from sentence_transformers import SentenceTransformer, util
from sqlalchemy import select
import torch
from database.models import Tour
from database.engine import session_maker
import asyncio

model = SentenceTransformer('all-MiniLM-L6-v2')

async def find_similar_tours(user_query: str, top_k: int = 3):
    async with session_maker() as session:
        tours = await session.execute(select(Tour))
        tours = tours.scalars().all()
        
        if not tours:
            return []

        # Формируем список описаний туров
        tour_descriptions = [
            f"{tour.country} {tour.city} {tour.description} {tour.tour_type} {tour.seasons}"
            for tour in tours
        ]
        
        # Генерируем эмбеддинги
        tour_embeddings = model.encode(tour_descriptions, convert_to_tensor=True)
        query_embedding = model.encode(user_query, convert_to_tensor=True)
        
        # Вычисляем косинусную схожесть
        cos_scores = util.cos_sim(query_embedding, tour_embeddings)[0]
        top_results = torch.topk(cos_scores, k=min(top_k, len(tours)))
        
        # Возвращаем топ-N туров
        return [tours[idx] for idx in top_results.indices]
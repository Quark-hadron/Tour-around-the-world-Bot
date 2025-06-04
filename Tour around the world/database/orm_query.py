from sqlalchemy import func, select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Tour, Tour_user


async def orm_get_tours(
    session: AsyncSession,
    count_people: int,
    season: str,
    tour_type: str
):
    # Преобразуем сезон и тип тура к нижнему регистру для унификации
    season = season.capitalize()
    tour_type = tour_type.capitalize()
    
    query = select(Tour).where(
        Tour.count_people == count_people,
        func.lower(Tour.seasons) == season,
        func.lower(Tour.tour_type) == tour_type
    )

    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_tour(session: AsyncSession, tour_id: int):
    query = select(Tour).where(Tour.id == tour_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_get_all_tours(session: AsyncSession):
    result = await session.execute(select(Tour))
    return result.scalars().all()


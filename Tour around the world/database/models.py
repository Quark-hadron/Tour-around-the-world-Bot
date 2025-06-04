from sqlalchemy import String, Text, Float, Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updates: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Tour(Base):
    __tablename__ = 'Tour'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    in_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    out_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    tour_type: Mapped[int] = mapped_column(Integer(), nullable=False)
    count_people: Mapped[int] = mapped_column(Integer(), nullable=False)
    country: Mapped[str] = mapped_column(String(150), nullable=False)
    city: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    seasons: Mapped[str] = mapped_column(String(150), nullable=False)
    image: Mapped[str] = mapped_column(String(150))
    rating: Mapped[float] = mapped_column(Float(), nullable=False)

class Base_user(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updates: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Tour_user(Base_user):
    __tablename__ = 'Tour_user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tour_type: Mapped[int] = mapped_column(Integer(), nullable=False)
    count_people: Mapped[int] = mapped_column(Integer(), nullable=False)
    seasons: Mapped[str] = mapped_column(String(150), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    tour_id: Mapped[int] = mapped_column(Integer(), nullable=True)


class UserWish(Base_user):
    __tablename__ = 'user_wish'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    wish_text: Mapped[str] = mapped_column(Text, nullable=False)
    processed: Mapped[bool] = mapped_column(default=False)    
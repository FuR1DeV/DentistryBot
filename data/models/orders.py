from sqlalchemy import Column, Integer, BigInteger, String, DECIMAL, sql, DateTime, TIMESTAMP

from data.db_gino import BaseModel


class Orders(BaseModel):
    __tablename__ = "orders"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    user_id_operator = Column(BigInteger, nullable=False)
    description = Column(String)
    create_task = Column(TIMESTAMP)
    get_task = Column(TIMESTAMP)
    user_id_manager = Column(BigInteger)
    done_task = Column(TIMESTAMP)


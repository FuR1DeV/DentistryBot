from sqlalchemy import Column, Integer, BigInteger, String, DECIMAL, sql, DateTime, TIMESTAMP

from data.db_gino import BaseModel


class Orders(BaseModel):
    __tablename__ = "orders"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    operator_user_id = Column(BigInteger, nullable=False)
    operator_name = Column(String)
    description = Column(String)
    create_task = Column(TIMESTAMP)
    get_task = Column(TIMESTAMP)
    manager_user_id = Column(BigInteger)
    manager_name = Column(String)
    done_task = Column(TIMESTAMP)


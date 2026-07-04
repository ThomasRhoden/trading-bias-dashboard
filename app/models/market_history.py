from sqlalchemy import Column, Integer, String, Float, DateTime
import datetime
from app.config.database import Base

class MarketHistory(Base):
    __tablename__ = "market_history"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    vies = Column(String)
    # Se quiser salvar o log detalhado aqui, você poderia usar um campo JSON, 
    # mas por enquanto vamos focar no estado do viés.
from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base

class AtivoB3(Base):
    __tablename__ = "ativos_b3"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, nullable=False)
    nome = Column(String, nullable=False)
    setor = Column(String)
    exchange = Column(String, default="BMFBOVESPA") # Ex: BMFBOVESPA, AMEX
    screener = Column(String, default="brazil")     # Ex: brazil, america
    is_ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<AtivoB3(ticker='{self.ticker}')>"
from app.config.database import SessionLocal
from app.models.ativos import AtivoB3

class AtivoDAO:
    """
    Responsável por gerenciar as operações de banco de dados para os ativos B3.
    """
    
    @staticmethod
    def adicionar_ativo(ticker, nome, setor):
        session = SessionLocal()
        try:
            novo_ativo = AtivoB3(ticker=ticker, nome=nome, setor=setor)
            session.add(novo_ativo)
            session.commit()
            print(f"Ativo {ticker} adicionado com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"Erro ao adicionar ativo {ticker}: {e}")
        finally:
            session.close()

    @staticmethod
    def listar_ativos_ativos():
        """Retorna apenas os ativos que estão com flag is_ativo=True"""
        session = SessionLocal()
        try:
            ativos = session.query(AtivoB3).filter(AtivoB3.is_ativo == True).all()
            return ativos
        finally:
            session.close()
# load_ibov.py
from app.config.database import SessionLocal
from app.models.ativos import AtivoB3

ativos_ibov = [
    "RRRP3", "ABEV3", "AERI3", "AESB3", "ALPA4", "ALSO3", "AMER3", "ARZZ3", "ASAI3", "AZUL4",
    "B3SA3", "BBAS3", "BBDC3", "BBDC4", "BBSE3", "BEEF3", "BPAC11", "BRAP4", "BRFS3", "BRKM5",
    "BRML3", "CCRO3", "CIEL3", "CMIG4", "CMIN3", "COGN3", "CPFE3", "CPLE6", "CRFB3", "CSAN3",
    "CSNA3", "CVCB3", "CYRE3", "DXCO3", "EGIE3", "ELET3", "ELET6", "EMBR3", "ENBR3", "ENGI11",
    "ENEV3", "ENGIE3", "EQTL3", "EZTC3", "FLRY3", "GGBR4", "GOAU4", "GOLL4", "HAPV3", "HYPE3",
    "IGTI11", "IRBR3", "ITUB4", "ITSA4", "JBSS3", "JHSF3", "KLBN11", "LREN3", "LWSA3", "MGLU3",
    "MRFG3", "MRVE3", "MULT3", "NTCO3", "PCAR3", "PETR3", "PETR4", "PETZ3", "PRIO3", "QUAL3",
    "RADL3", "RAIL3", "RAIZ4", "RDOR3", "RENT3", "SANB11", "SBSP3", "SIMH3", "SLCE3", "SOMA3",
    "SUZB3", "TAEE11", "TIMS3", "TOTS3", "UGPA3", "USIM5", "VALE3", "VBBR3", "WEGE3", "YDUQ3"
]

def carregar_ativos():
    session = SessionLocal()
    print(f"Iniciando importação de {len(ativos_ibov)} ativos...")
    
    count = 0
    for ticker in ativos_ibov:
        # Verifica se já existe
        existe = session.query(AtivoB3).filter_by(ticker=ticker).first()
        if not existe:
            novo = AtivoB3(
                nome=f"Ativo {ticker}", 
                ticker=ticker, 
                exchange="B3", 
                screener="brazil"
            )
            session.add(novo)
            count += 1
            
    session.commit()
    session.close()
    print(f"Sucesso: {count} novos ativos inseridos no banco.")

if __name__ == "__main__":
    carregar_ativos()
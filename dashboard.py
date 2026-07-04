import streamlit as st
import pandas as pd
from app.models.market_engine import MarketEngine
from app.dao.market_data_dao import MarketDataDAO

st.set_page_config(page_title="Monitor IBOVESPA", layout="wide")

st.title("📊 Monitor IBOVESPA - 88 Ativos")

# Busca o último viés calculado pelo worker
ultimo_dado = MarketDataDAO.buscar_ultimo_registro()
if ultimo_dado:
    st.metric("Viés Atual do Mercado", ultimo_dado.vies)
else:
    st.warning("Aguardando worker calcular o viés...")

st.markdown("---")

# Exibição dos ativos
st.subheader("Ativos Monitorados")

# Botão para forçar atualização (o engine tem cache, então é seguro)
if st.button("Atualizar Agora"):
    engine = MarketEngine()
    dados = engine.obter_dados_mercado()
    df = pd.DataFrame.from_dict(dados['ativos'], orient='index')
    st.dataframe(df, use_container_width=True)
else:
    st.info("Clique no botão acima para carregar a cotação dos 88 ativos.")
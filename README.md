# 📊 Trading Bias Dashboard

> Um painel macroeconômico construído em Python (Flask) utilizando o padrão arquitetural MVC, desenhado para leitura de mercado pré-abertura.

## 🎯 Sobre o Projeto
Este sistema foi desenvolvido para consolidar dados macroeconômicos globais, fornecendo um viés estatístico direcional para o dia de operações. Criado com foco na separação estrita de responsabilidades (MVC - Model, View, Controller), o projeto serve tanto como uma ferramenta de apoio analítico (ideal para rodar em paralelo com plataformas de trading) quanto como um sólido case de desenvolvimento de software.

## ✨ Funcionalidades
- **Integração Externa:** Dados brutos capturados da API pública do TradingView (AMEX, BMFBOVESPA).
- **Processamento de Viés Macro:** Algoritmo que avalia o peso da variação de ativos-chave (SPY, USO, EWZ, VALE3) para entregar uma bússola de mercado.
- **Arquitetura MVC:** Código modular e escalável.

## 🚀 Tecnologias Utilizadas
- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Engine de Dados:** `tradingview_ta`

## 🛠️ Como Rodar o Projeto Localmente

**1. Clone o repositório**
```bash
git clone [https://github.com/ThomasRhoden/trading-bias-dashboard.git](https://github.com/ThomasRhoden/trading-bias-dashboard.git)
cd trading-bias-dashboard
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Inicie o Servidor**
```bash
python main.py
```
*O dashboard estará disponível no navegador em http://127.0.0.1:5000*
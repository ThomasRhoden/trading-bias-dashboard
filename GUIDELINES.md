# 📘 Diretrizes do Projeto: Trading Bias Dashboard

Este documento define os padrões de código, arquitetura e versionamento para o desenvolvimento sustentável deste projeto.

## 🏗️ Arquitetura (Padrão MVC)
- **Models (`app/models/`):** Regras de negócio, cálculos matemáticos e comunicação com APIs externas (ex: TradingView). NENHUMA regra de interface deve estar aqui.
- **Controllers (`app/controllers/`):** O "meio-campo". Recebe as requisições web (Rotas do Flask), chama o Model necessário e devolve os dados para a View.
- **Views (`app/views/templates/`):** Exclusivo para HTML/CSS/JS. Responsável apenas por exibir os dados processados na tela.

## 📝 Padrão de Commits (Conventional Commits)
Cada commit deve seguir a semântica abaixo para gerar um histórico limpo e profissional:
- `feat:` Nova funcionalidade (ex: `feat: adiciona ativo DXY ao painel`)
- `fix:` Correção de bug (ex: `fix: corrige erro 429 de limite da API`)
- `docs:` Alterações apenas em documentação (ex: `docs: atualiza README com instruções de instalação`)
- `refactor:` Refatoração de código que não adiciona feature nem corrige bug (ex: `refactor: melhora loop de requisição no market_engine`)
- `style:` Formatação, ponto e vírgula, etc. (não afeta o código)

## 🐍 Padrão de Código Python (PEP 8)
- Nomes de variáveis e funções: `snake_case` (ex: `obter_dados_mercado`).
- Nomes de classes: `PascalCase` (ex: `MarketEngine`).
- Todo método complexo deve possuir `Docstrings` explicando o que faz, o que recebe e o que retorna.
- Tratamento de exceções (`try/except`) é obrigatório em requisições de rede.

## 🗺️ Roadmap de Desenvolvimento
- [x] Estruturação do MVC e servidor Flask.
- [x] Integração com API do TradingView para S&P 500, Petróleo, EWZ e VALE3.
- [ ] Implementação de sistema de cache para evitar requisições desnecessárias.
- [ ] Refinamento de UI/UX (Ícones, Modo Dark/Light).
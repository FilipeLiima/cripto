# Projeto de Análise de Criptoativos

## Neste projeto, a análise de criptoativos será conduzida através da obtenção de dados de uma API. Identificaremos os criptoativos que apresentaram maior valorização e aqueles que demonstram tendência de valorização com base nos dados gerados. Implementaremos um modelo de machine learning integrado a esses dados em tempo real, visando fornecer previsões e insights para auxiliar a tomada de decisões dos investidores. Adicionalmente, desenvolveremos um banco de dados dedicado, no qual informações relacionadas à carteira de investimentos serão gravadas e armazenadas. Esse sistema utilizará um banco de dados SQL e possibilitará o acesso a informações essenciais sobre a carteira, promovendo uma gestão eficiente dos investimentos. O objetivo principal do projeto é fornecer aos investidores uma plataforma robusta e dinâmica, permitindo análises detalhadas, previsões precisas e gerenciamento eficaz de suas carteiras de criptoativos.

### Roadmap:

1. Primeiro ponto: montar a estrutura de obtenção dos dados por meio da API da coingecko;
2. Definir quais variáveis de análise devo considerar no request;
   - Informações Gerais sobre Criptoativos: rota /coins/list
   - Preços e Volumes: /coins/markets
   - Dados Históricos: rota /coins/{id}/market_chart/range
3. Salvar esses dados em formato JSON devido a estrutura hierárquica complexa (pré processar esses dados posteriormente);
4. Construir dash interativos que oferecem insights
5. Construir modelo de machine learning que consiga gerar previsões em tempo real;
6. Construir banco de dados para funcionar como carteira;
7. Plotar tudo em streamlit.

RESUMO
requisição de consumo de dados e rotas - ok
definição de variáveis de análise - ok
salvamento de dados de variáveis em JSON - ok
construção de um dash para oferecer insights = falta na parte de home mais informações sobre o ativo, muito mais.

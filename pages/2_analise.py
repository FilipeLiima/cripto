import streamlit as st
import plotly.graph_objects as go
from api_requests import get_crypto_data
import pandas as pd


def plot_price_volume_chart(price_data, volume_data):
    fig = go.Figure()

    # Adicione um gráfico de linhas para o preço
    fig.add_trace(
        go.Scatter(
            x=price_data.index, y=price_data["preco"], mode="lines", name="Preço"
        )
    )

    # Adicione um gráfico de barras para o volume
    fig.add_trace(go.Bar(x=volume_data.index, y=volume_data["volume"], name="Volume"))

    # Personalize o layout do gráfico
    fig.update_layout(
        title_text="Histórico de Preço e Volume",
        xaxis_title="Data",
        yaxis_title="Valor",
    )

    return fig


def analise():
    st.write("## Análise de Criptoativos")

    # Menu 2: Análise
    st.sidebar.header("")
    selected_crypto_analise = st.sidebar.selectbox(
        "Selecione um ativo:", ["bitcoin", "ethereum", "outro-ativo"], key="analise"
    )
    crypto_data_analise = get_crypto_data(selected_crypto_analise.lower())

    if crypto_data_analise:
        # Exibe gráficos e informações de análise sobre o histórico de preço e volume
        st.write(f"**Análise de {selected_crypto_analise}:**")

        # Obtenha os dados históricos de preço e volume
        price_data = pd.DataFrame(crypto_data_analise.get("historico_precos", {}))
        volume_data = pd.DataFrame(crypto_data_analise.get("historico_volumes", {}))

        if price_data.empty or volume_data.empty:
            st.warning("Os dados históricos não estão disponíveis para gerar gráficos.")
        else:
            # Crie e exiba os gráficos
            st.plotly_chart(plot_price_volume_chart(price_data, volume_data))

        # ... adicione outras informações para análise


if __name__ == "__main__":
    analise()

import streamlit as st


def previsoes():
    st.title("Análise de Criptoativos - Previsões")

    # Menu 3: Previsões (no sidebar)
    st.sidebar.header("Menu 3: Previsões")
    # Exibe modelo de machine learning para previsões
    st.sidebar.write("**Previsões:**")
    # ... adicione o modelo de machine learning e as previsões


if __name__ == "__main__":
    previsoes()

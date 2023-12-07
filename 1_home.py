import streamlit as st
from api_requests import get_general_info
from googletrans import Translator
from bs4 import BeautifulSoup


def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def translate_to_portuguese(text):
    translator = Translator()
    translation = translator.translate(text, dest="pt")
    return translation.text


def home():
    st.write("## Informações gerais sobre criptoativos")

    # Menu 1: Home
    st.subheader("")

    selected_crypto_home = st.sidebar.selectbox(
        "Selecione um ativo:",
        ["bitcoin", "ethereum", "outro-ativo"],
        index=None,
        key="home",
        placeholder="Selecione um ativo...",
    )

    if selected_crypto_home:
        # Garante que o valor não é None antes de chamar lower()
        crypto_data_home = get_general_info(selected_crypto_home.lower())

        if crypto_data_home:
            # Exibe informações gerais sobre a moeda na direita da tela
            st.write(
                f"**Informações Gerais sobre {crypto_data_home.get('name', 'Desconhecido')}:**"
            )
            st.write(f"Símbolo: {crypto_data_home.get('symbol', 'Desconhecido')}")
            st.write(f"Nome: {crypto_data_home.get('name', 'Desconhecido')}")

            # Se a descrição em português estiver disponível, use-a; caso contrário, traduza a descrição em inglês
            description_pt = crypto_data_home.get("descricao", {}).get("pt", None)
            description_en = crypto_data_home.get("descricao", {}).get("en", None)

            if description_pt:
                cleaned_description = remove_html_tags(description_pt)
            elif description_en:
                cleaned_description = remove_html_tags(
                    translate_to_portuguese(description_en)
                )
            else:
                cleaned_description = "Descrição não disponível."

            st.write(f"Descrição: {cleaned_description}")
            # ... adicione outras informações que você deseja exibir


if __name__ == "__main__":
    home()

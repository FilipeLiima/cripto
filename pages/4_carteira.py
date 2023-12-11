import streamlit as st
from db import conectar_banco, consultar_ativos_detalhes, adicionar_ativo
from datetime import datetime
from decimal import Decimal
import pandas as pd

# Função para obter a lista local de criptoativos
def get_crypto_list_local():
    return ["BTC", "ETH", "LTC", "XRP", "ADA", "DOT", "BCH", "LINK", "BNB", "XLM"]

def excluir_ativo(conn, ativo_id):
    # Lógica para excluir o ativo no banco de dados
    # Substitua isso pela lógica real para excluir no seu banco de dados
    # Exemplo fictício:
    # conn.execute(f"DELETE FROM ativos WHERE id = {ativo_id}")
    pass

def format_decimal(decimal_value):
    return float(decimal_value)

def format_datetime(datetime_value):
    return datetime_value.strftime("%Y-%m-%d %H:%M:%S") if datetime_value else None

def main():
    st.title("Carteira do investidor")

    # Conectar ao banco de dados
    conn = conectar_banco()

    # Dividindo a tela em duas colunas
    col1, col2 = st.columns(2)

    # Adicionando elementos à primeira coluna
    with col1:
        criptoativos_disponiveis = get_crypto_list_local()

        # Consultar ativos no banco de dados
        ativos = consultar_ativos_detalhes(conn)

        opcao = st.selectbox("Selecione o ativo", criptoativos_disponiveis, index=None, placeholder="Seleção...")
        quantidade = st.number_input("Quantidade comprada", min_value=0.01, step=0.01, format="%.2f")
        valor_pago = st.number_input("Valor pago", min_value=0.01, step=0.01, format="%.2f")
        st.write('Você selecionou:', opcao)

        # Botão para adicionar ativo ao banco de dados
        if st.button("Adicionar Ativo"):
            adicionar_ativo(conn, opcao, quantidade, valor_pago)
            st.success(f"Ativo {opcao} adicionado com sucesso!")

        # Botão para excluir ativo
        if st.button("Excluir Ativo"):
            # Opção para selecionar qual ativo excluir
            opcao_excluir = st.selectbox("Selecione o ativo para excluir", [ativo[0] for ativo in ativos])

            # Encontrar todos os IDs do ativo selecionado
            ids_para_excluir = [ativo[1] for ativo in ativos if ativo[0] == opcao_excluir]

            # Verificar se há IDs a serem excluídos
            if ids_para_excluir:
                # Iterar sobre os IDs e excluir cada um
                for ativo_id_excluir in ids_para_excluir:
                    excluir_ativo(conn, ativo_id_excluir)

                st.success(f"Ativo {opcao_excluir} excluído com sucesso!")
            else:
                st.warning(f"Ativo {opcao_excluir} não encontrado para exclusão.")



    # Restante do código...
    st.write("Lista de Ativos na Carteira:")

    # Criar uma lista para armazenar os dados formatados
    formatted_data = []

    # Iterar sobre as transações e adicionar dados formatados à lista
    for ativo in ativos:
        formatted_data.append({
            "Ativo": ativo[0],
            "Usuário ID": ativo[1],
            "Quantidade": format_decimal(ativo[2]),
            "Valor Pago": format_decimal(ativo[3]),
            "Data Transação": format_datetime(ativo[4]),
        })

    # Criar um DataFrame Pandas com os dados formatados
    df = pd.DataFrame(formatted_data)

    # Exibir a tabela no Streamlit
    st.table(df)

    # Fechar conexão
    conn.close()

if __name__ == "__main__":
    main()

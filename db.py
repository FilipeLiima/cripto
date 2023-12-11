import psycopg2
from datetime import datetime
import streamlit as st

def conectar_banco():
    """
    Função para conectar ao banco de dados.
    """
    conn = psycopg2.connect(
        dbname="InvestorDB",
        user="postgres",
        password="1992",
        host="localhost",
        port="5432"
    )
    return conn

def adicionar_ativo(conn, nome, quantidade, valor_pago):
    try:
        # Verifica se o nome do ativo é válido
        if nome:
            with conn.cursor() as cursor:
                # Adiciona o ativo sem especificar valor_atual
                cursor.execute("INSERT INTO ativos (nome, valor_atual) VALUES (%s, %s) RETURNING id", (nome, 0.0))
                ativo_id = cursor.fetchone()[0]

                # Agora, insira a transação associada ao ativo
                cursor.execute(
                    "INSERT INTO transacoes (usuario_id, ativo_id, quantidade, valor_pago) VALUES (%s, %s, %s, %s)",
                    (1, ativo_id, quantidade, valor_pago),
                )

            # Commit para salvar as alterações no banco de dados
            conn.commit()
        else:
            print("Nome do ativo inválido. Não foi possível adicionar ativo.")
    except Exception as e:
        # Em caso de erro, imprima a mensagem de erro
        print(f"Erro ao adicionar ativo: {e}")
        # Faça rollback para desfazer quaisquer alterações pendentes
        conn.rollback()
def consultar_ativos_detalhes(conn):
    # Função para consultar detalhes de ativos na carteira a partir do banco de dados
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            a.nome AS ativo,
            t.usuario_id,
            t.quantidade,
            t.valor_pago,
            t.data_transacao
        FROM
            transacoes t
        JOIN
            ativos a ON t.ativo_id = a.id
    """)
    
    result = cursor.fetchall()
    cursor.close()
    return result



def main():
    st.title("Consulta ao Banco de Dados")

    # Conectar ao banco de dados
    conn = conectar_banco()

    # Exemplo de consulta: selecionar todos os ativos
    ativos = consultar_ativos_detalhes(conn)

    # Exibir resultados no Streamlit
    st.write("Lista de Ativos:")
    st.write(ativos)

    # Fechar conexão
    conn.close()

if __name__ == "__main__":
    main()

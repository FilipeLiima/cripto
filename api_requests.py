import os
import requests
import json

def get_crypto_list():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False,
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 429:
            print("Muitas requisições. Aguarde um momento e tente novamente.")
            return []
        elif response.status_code == 200:
            crypto_list = response.json()
            return [crypto['symbol'].upper() for crypto in crypto_list]
        else:
            print(f"Falha ao obter a lista de criptoativos. Status Code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Falha ao obter a lista de criptoativos: {e}")
        return []


def get_crypto_data(crypto_id):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Falha ao obter dados para {crypto_id}. Status Code: {response.status_code}"
        )
        return None

def get_general_info(crypto_id, language="en"):
    url_info = f"https://api.coingecko.com/api/v3/coins/{crypto_id}"
    url_chart = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"

    response_info = requests.get(url_info)
    response_chart = requests.get(url_chart)

    if response_info.status_code == 200 and response_chart.status_code == 200:
        crypto_info = response_info.json()
        chart_data = response_chart.json()
    else:
        print(
            f"Falha ao obter dados gerais para {crypto_id}. Status Code: {response_info.status_code}"
        )
        return None

    name = crypto_info.get("name", "Desconhecido")
    symbol = crypto_info.get("symbol", "Desconhecido")

    description_en = crypto_info.get("description", {}).get("en", "")
    translated_description = description_en  # Manter a descrição original em inglês

    print(f"Informações Gerais sobre {name} ({symbol}):")
    print(f"Símbolo: {symbol}")
    print(f"Nome: {name}")

    crypto_data = {
        "id": crypto_info["id"],
        "nome": name,
        "simbolo": symbol,
        "preco": None,
        "historico_precos": chart_data.get("prices", []),
        "historico_volumes": chart_data.get("total_volumes", []),
        "descricao": {
            "en": description_en,
            "pt": translated_description,
        },
    }

    return crypto_data

def save_to_json(data, file_path):
    data_folder = os.path.join(os.getcwd(), "data")

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    full_file_path = os.path.join(data_folder, file_path)

    with open(full_file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    # Exemplo de uso para uma criptomoeda (substitua 'unknown' por outra criptomoeda se desejar)
    crypto_data = get_general_info("bitcoin")

    if crypto_data:
        print(json.dumps(crypto_data, indent=2))
        save_to_json(crypto_data, "crypto_data.json")

import json

# Função para ler o JSON e salvar os valores de "seuNumero" em um arquivo .txt
def salvar_seu_numeros_em_txt(caminho_arquivo_json, caminho_arquivo_saida):
    try:
        # Abre o arquivo JSON para leitura
        with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)  # Carrega o JSON
        
        # Verifica se é uma lista e extrai os "seuNumero"
        if isinstance(dados, list):
            seus_numeros = [item.get("seuNumero", "Chave 'seuNumero' não encontrada") for item in dados]
        else:
            return "O arquivo JSON não contém uma lista de objetos."

        # Salva os valores no arquivo .txt
        with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            for numero in seus_numeros:
                arquivo_saida.write(f"{numero}\n")

        return f"Arquivo '{caminho_arquivo_saida}' criado com sucesso!"
    except FileNotFoundError:
        return "Arquivo JSON não encontrado."
    except json.JSONDecodeError:
        return "Erro ao processar o arquivo JSON."

# Caminho do arquivo JSON e do arquivo de saída
caminho_json = "jsonList.json"
caminho_saida = "seu_numeros9.txt"

# Chama a função e imprime o resultado
resultado = salvar_seu_numeros_em_txt(caminho_json, caminho_saida)
print(resultado)

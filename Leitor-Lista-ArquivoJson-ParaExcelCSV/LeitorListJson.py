import json
import os
import pandas as pd

def processar_json_para_relatorio(pasta_json, arquivo_saida):
    dados = []
    
    # Itera sobre os arquivos JSON na pasta
    for arquivo in os.listdir(pasta_json):
        if arquivo.endswith('.json'):
            caminho_arquivo = os.path.join(pasta_json, arquivo)
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                try:
                    # Carrega o conteúdo do arquivo JSON
                    conteudo = json.load(f)
                    for item in conteudo:
                        # Adiciona apenas os campos necessários
                        dados.append({
                            "seuNumero": item.get("seuNumero"),
                            "tipoOpFinanceira": item.get("tipoOpFinanceira")
                        })
                except json.JSONDecodeError as e:
                    print(f"Erro ao processar o arquivo {arquivo}: {e}")
    
    # Cria um DataFrame com os dados
    df = pd.DataFrame(dados)
    
    # Salva no formato especificado (CSV ou Excel)
    if arquivo_saida.endswith('.csv'):
        df.to_csv(arquivo_saida, index=False, encoding='utf-8-sig')
    elif arquivo_saida.endswith('.xlsx'):
        df.to_excel(arquivo_saida, index=False, engine='openpyxl')
    else:
        print("Formato de saída não suportado. Use '.csv' ou '.xlsx'.")

# Exemplo de usoLeitor-Lista-ArquivoJson-ParaExcelCSV\JsonListArquivo
pasta_json = '..\Leitor-Lista-ArquivoJson-ParaExcelCSV\JsonListArquivo'  # Substitua pelo caminho da pasta com os arquivos JSON
arquivo_saida = 'relatorio2.xlsx'  # Pode ser 'relatorio.xlsx' para Excel
processar_json_para_relatorio(pasta_json, arquivo_saida)

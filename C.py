import json

def carregar_dados_json(caminho_arquivo):
    arquivo = open(caminho_arquivo, 'r')
    dados = json.load(arquivo)
    arquivo.close()
    return [linha['valor'] for linha in dados['faturamento_diario'] if linha['valor'] > 0]

def calcular_faturamento(faturamento_diario):
    if not faturamento_diario:
        return {"mensagem": "Nenhum dado de faturamento disponível."}
    
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

faturamento_diario = carregar_dados_json('faturamento.json')
resultados = calcular_faturamento(faturamento_diario)

if "mensagem" in resultados:
    print(resultados["mensagem"])
else:
    print(f"Menor valor de faturamento: R${resultados['menor_faturamento']:.2f}")
    print(f"Maior valor de faturamento: R${resultados['maior_faturamento']:.2f}")
    print(f"Número de dias com faturamento acima da média: {resultados['dias_acima_media']}")

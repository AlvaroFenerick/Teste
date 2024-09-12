def calcular_percentuais(faturamento_estado):
    total = sum(faturamento_estado.values())
    return {estado: (valor / total) * 100 for estado, valor in faturamento_estado.items()}

faturamento_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

percentuais = calcular_percentuais(faturamento_estado)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

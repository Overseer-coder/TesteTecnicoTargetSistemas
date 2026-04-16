def recuperar_maior_valor(faturamento):
    return max(faturamento)

def recuperar_menor_valor(faturamento):
    return min(faturamento)

def filtrar_sem_faturamento(faturamento):
    return list(filter(lambda valor : valor > 0, faturamento))

def filtrar_dias_maiores_media(faturamento, media):
    return list(filter(lambda valor: valor > media, faturamento_filtrado ))

if __name__ == "__main__":
    faturamento = [2, 1, 2, 0, 4, 0, 5, 0, 0, 4, 5, 0, 6, 7]

    faturamento_filtrado = filtrar_sem_faturamento(faturamento)

    media = sum(faturamento_filtrado)/len(faturamento_filtrado)

    num_dias_superiores_media = filtrar_dias_maiores_media(faturamento_filtrado, media)

    print("A média do faturamento é ", media)
    print(f"Em {len(num_dias_superiores_media)} dias o valor de faturamento foi maior que a média")
    print("O maior valor do faturamento é ", recuperar_maior_valor(faturamento_filtrado))
    print("O menor valor do faturamento é ", recuperar_menor_valor(faturamento_filtrado))
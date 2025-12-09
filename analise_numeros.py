# analise_numeros.py
# Programa que analisa uma lista de números usando for e while

def main():
    # Lista de números para análise
    numeros = [15, 8, 23, 4, 42, 16, 31, 7, 50, 12]

    print("=== ANÁLISE DE NÚMEROS ===\n")
    print(f"Lista original: {numeros}\n") 

    # Usando FOR para calcular soma e encontrar o maior número
    soma = 0
    maior = numeros[0]

    print("--- Usando FOR ---")
    for num in numeros:
        soma += num
        if num > maior:
            maior = num
        print(f"Processando: {num}")

    media = soma / len(numeros)
    print(f"\nSoma total: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior}\n")

    # Usando WHILE para contar números pares
    print("--- Usando WHILE ---")
    indice = 0
    pares = []

    while indice < len(numeros):
        if numeros[indice] % 2 == 0:
            pares.append(numeros[indice])
            print(f"Número par encontrado: {numeros[indice]}")
        indice += 1

    print(f"\nTotal de números pares: {len(pares)}")
    print(f"Números pares: {pares}")

if __name__ == "__main__":
    main()
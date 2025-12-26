# Programa que processa apenas números pares de uma lista
# Números ímpares são pulados (continue)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Processando apenas números PARES:")
print("-" * 40)

for numero in numeros:
    # Se o número for ímpar, pula para a próxima iteração
    if numero % 2 != 0:
        print(f"{numero} é impar - pulando...")
        continue # Pulaa o resto do código e vai para o próximo número

    # Este código só executa para números pares
    print(f"{numero} é PAR - processando...")
    resultado = numero * 2
    print(f"   {numero} x 2 = {resultado}")
    
print("\Processamento concluido!\n")

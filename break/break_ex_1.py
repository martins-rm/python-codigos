# Programa que busca um número específico em uma lista
# Quando encontrar o número, para a busca (break)

numeros = [5, 12, 8, 23, 15, 30, 7, 19]
numero_procurado = 15

print('Procurando o número', numero_procurado, 'na lista...')

for numero in numeros:
    print(f'Verificando: {numero}')

# Se encontrar o número procurado, para a execução do loop
    if numero == numero_procurado:
        print(f'Número {numero_procurado} encontrado!')
        break # Sai do loop imediatamente

    print(f'    {numero} não é o numero procurado, continuando ....')
print('Busca finalizada!\n')
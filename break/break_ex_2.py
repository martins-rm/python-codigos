# Exemplo de sistema de login com tentativas limitadas
print("=" * 40)
print("SISTEMA DE LOGIN")
print("=" * 40)

senha_correta = "python123"
tentativas_maximas = 3

for tentativa in range(1,tentativas_maximas + 1):
    print(f"\nTentativa {tentativa} de {tentativas_maximas}")
    senha = input("Digite a senha: ")

    # Se acertar a senha, sai do loop
    if senha == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        print("Senha incorreta")

        # Se esgotou as tentativas
        if tentativa == tentativas_maximas:
            print("\nNúmero máximo de tentativas excedido!")
            print("Acesso bloqueado.")

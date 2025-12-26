# Outro exemplo prático: validação de emails em uma lista

print("=" * 40)
print("VALIDADOR DE EMAILS")
print("=" * 40)

emails = [
    "joao@email.com",
    "maria.email.com",   # Email inválido (sem @)
    "pedro@company.com",
    "ana@",              # Email inválido (incompleto)
    "carlos@site.com.br",
    ""                   # Email vazio
]

emails_validos = []

for email in emails:
    print(f"\nVerificando: '{email}'")

    # Pula emails vazios
    if email == "":    
        print(f" Email vazio - ignorando...")
        continue # Vai para o próximo email

    # Pula emails sem @
    if "@" not in email:
        print("x Email inválido (sem @) - ignorando...")
        continue

    # Pula emails que terminam com @
    if email.endswith("@"):
        print(" x Email incompleto ignorando...")
        continue # Vai para o próximo email

    # Se passou por todas as verificações, o email é válido
    print(f" Email válido!")
    emails_validos.append(email)

print("\n" + "=" * 40)
print(f"Total de emails válidos: {len(emails_validos)}")
print("Emails válidos:", emails_validos)




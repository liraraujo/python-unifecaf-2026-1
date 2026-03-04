login = "admin"
senha = "1234"


if login == "admin" and senha == "1234":
    print("Acesso total concedido.")
else:
    print("Acesso restrito. Verifique suas credenciais.")

if login == "gerente" and senha == "1234":
    print("Acesso concedido para gerente.")
else:
    print("Acesso restrito. Verifique suas credenciais.")

if login == "vendedor" and senha == "1234":
     print("Acesso concedido para vendedor.")
else:
    print("Acesso restrito. Verifique suas credenciais.")
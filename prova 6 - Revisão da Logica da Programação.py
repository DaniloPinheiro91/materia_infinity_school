usuario_correto = "joao.empresa"
senha_correta = "123senha"
tentativas = 3


for i in range(tentativas):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("acesso permitido!")
        break
    else:
        tentativas_restantes = tentativas - (i + 1)
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você tem {tentativas_restantes} tentativa(s) restante(s).")
        else:
           print("Você errou as 3 tentativas, acesso não permitido.")

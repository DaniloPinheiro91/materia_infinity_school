import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.scroll = "auto"

    # Campos do formulário
    nome_input = ft.TextField(label="Nome", width=400)
    email_input = ft.TextField(label="Email", width=400)
    mensagem_input = ft.TextField(label="Mensagem", multiline=True, min_lines=4, width=400)

    # Texto de confirmação
    confirmacao_texto = ft.Text("", color="green")

    # Função chamada ao clicar no botão
    def enviar_formulario(e):
        if nome_input.value and email_input.value and mensagem_input.value:
            confirmacao_texto.value = "Formulário enviado com sucesso!"
            #sistema para salvar dados(não implementado nesse codigo)
            nome_input.value = ""
            email_input.value = ""
            mensagem_input.value = ""
        else:
            confirmacao_texto.value = "Por favor, preencha todos os campos!"
            confirmacao_texto.color = "red"
        page.update()

    # Botão de envio
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    # Layout
    page.add(
        ft.Column(
            controls=[
                nome_input,
                email_input,
                mensagem_input,
                botao_enviar,
                confirmacao_texto
            ],
            spacing=15,
            alignment="start"
        )
    )

ft.app(target=main)
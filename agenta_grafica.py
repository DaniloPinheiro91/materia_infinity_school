import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.scroll = "auto"

    #Onde serão exibidas as tarefas adicionadas
    tarefas = ft.Column()

    #Ação ao clicar o botão
    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != "":
            tarefas.controls.append(ft.Text(campo_tarefa.value))
            campo_tarefa.value = ""  # Limpa o campo de entrada
            page.update()

    #Entrada de texto
    campo_tarefa = ft.TextField(
        label="Digite uma nova tarefa",
        hint_text="Ex: Estudar Python",
        expand=True
    )

    #Botão para adicionar tarefa
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar",
        on_click=adicionar_tarefa
    )

    
    page.add(
        ft.Row([campo_tarefa, botao_adicionar]),
        tarefas
    )
ft.app(target=main)
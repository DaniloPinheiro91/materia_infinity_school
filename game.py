import flet as ft
import hashlib
import json
import os

ARQUIVO_USUARIOS = "usuarios.json"

# Função de hash
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Carregar ou criar arquivo de usuários
def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "w") as f:
            json.dump({}, f)
    with open(ARQUIVO_USUARIOS, "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

def login_screen(page: ft.Page):
    page.clean()
    usuarios = carregar_usuarios()

    nome_input = ft.TextField(label="Nome de usuário")
    senha_input = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    status_text = ft.Text("")

    def autenticar(e):
        usuario = nome_input.value.lower()
        senha = senha_input.value

        if usuario in usuarios and hash_senha(senha) == usuarios[usuario]:
            status_text.value = "✅ Login bem-sucedido!"
            page.clean()
            personagem_screen(page, usuario)
        else:
            status_text.value = "❌ Usuário ou senha inválidos."
        page.update()

    def registrar(e):
        registro_screen(page)

    login_btn = ft.ElevatedButton(text="Entrar", on_click=autenticar)
    registrar_btn = ft.TextButton(text="Criar nova conta", on_click=registrar)

    page.add(
        ft.Column([
            ft.Text("🔐 Login de Acesso", size=24, weight="bold"),
            nome_input,
            senha_input,
            login_btn,
            registrar_btn,
            status_text
        ], spacing=20, alignment="center")
    )

def registro_screen(page: ft.Page):
    page.clean()
    usuarios = carregar_usuarios()

    nome_input = ft.TextField(label="Novo nome de usuário")
    senha_input = ft.TextField(label="Nova senha", password=True, can_reveal_password=True)
    status_text = ft.Text("")

    def criar_usuario(e):
        usuario = nome_input.value.lower()
        senha = senha_input.value

        if not usuario or not senha:
            status_text.value = "⚠️ Preencha todos os campos."
        elif usuario in usuarios:
            status_text.value = "⚠️ Usuário já existe."
        else:
            usuarios[usuario] = hash_senha(senha)
            salvar_usuarios(usuarios)
            status_text.value = "✅ Conta criada com sucesso!"
        page.update()

    def voltar(e):
        login_screen(page)

    page.add(
        ft.Column([
            ft.Text("📝 Registro de Novo Usuário", size=24, weight="bold"),
            nome_input,
            senha_input,
            ft.ElevatedButton(text="Criar Conta", on_click=criar_usuario),
            ft.TextButton(text="← Voltar ao login", on_click=voltar),
            status_text
        ], spacing=20, alignment="center")
    )

def personagem_screen(page: ft.Page, usuario: str):
    page.title = f"Bem-vindo, {usuario.capitalize()}"

    class Personagem:
        def __init__(self, nome, vida=100, mana=50, forca=10):
            self.nome = nome
            self.vida = vida
            self.vida_max = vida
            self.mana = mana
            self.forca = forca

        def atacar(self, inimigo):
            dano = self.forca
            inimigo.vida = max(inimigo.vida - dano, 0)
            return f"{self.nome} atacou {inimigo.nome} causando {dano} de dano."

        def usar_magia(self, inimigo):
            if self.mana >= 10:
                dano = 25
                inimigo.vida = max(inimigo.vida - dano, 0)
                self.mana -= 10
                return f"{self.nome} lançou magia em {inimigo.nome} causando {dano} de dano."
            else:
                return f"{self.nome} tentou usar magia, mas não tem mana suficiente."

        def status(self):
            return f"{self.nome} - Vida: {self.vida}/{self.vida_max}, Mana: {self.mana}"

    heroi = Personagem(usuario.capitalize(), forca=15)
    monstro = Personagem("Goblin", vida=80, forca=8)

    status_heroi = ft.Text(heroi.status())
    barra_vida_heroi = ft.ProgressBar(width=300, value=1.0, color="green")

    status_monstro = ft.Text(monstro.status())
    barra_vida_monstro = ft.ProgressBar(width=300, value=1.0, color="red")

    log = ft.Text("", size=14, selectable=True)

    def atualizar_tela(mensagem):
        status_heroi.value = heroi.status()
        status_monstro.value = monstro.status()
        barra_vida_heroi.value = heroi.vida / heroi.vida_max
        barra_vida_monstro.value = monstro.vida / monstro.vida_max
        log.value = mensagem
        page.update()

    def atacar_click(e):
        msg = heroi.atacar(monstro)
        atualizar_tela(msg)

    def magia_click(e):
        msg = heroi.usar_magia(monstro)
        atualizar_tela(msg)

    def ver_status_click(e):
        atualizar_tela("Status atualizados.")

    btn_atacar = ft.ElevatedButton(text="Atacar", on_click=atacar_click)
    btn_magia = ft.ElevatedButton(text="Usar Magia", on_click=magia_click)
    btn_status = ft.ElevatedButton(text="Ver Status", on_click=ver_status_click)

    page.add(
        ft.Column([
            ft.Text(f"⚔️ Personagem: {heroi.nome}", size=24, weight="bold"),
            ft.Text("🧙‍♂️ Herói"),
            status_heroi,
            barra_vida_heroi,
            ft.Text("👹 Monstro"),
            status_monstro,
            barra_vida_monstro,
            ft.Row([btn_atacar, btn_magia, btn_status], spacing=20),
            ft.Text("🎮 Log de Batalha:", size=16),
            log
        ], spacing=20)
    )

# Iniciar app
ft.app(target=login_screen)
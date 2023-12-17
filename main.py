import mysql.connector
import flet as ft

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro',
)

cursor = conexao.cursor()
comand = 'INSERT INTO login_ (nome) VALUES ("{nome}")'
cursor.execute(comand)

def main(page):

    page.title = "Login employee"
    page.scroll= 'adptive'
    title_main = ft.Text(
        value='Login',
        color='green',
        text_align= ft.TextAlign.CENTER,
        width=1500,
        height=50,
        size=30,
    )
    page.add(title_main)

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your Login name"
            page.update()
        elif txt_name.value != "miles":
            txt_name.error_text = "Error"
            page.update()
        elif not txt_password.value:
            txt_password.error_text = "Please enter your password"
            page.update()
        elif txt_password.value != "123456":
            txt_password.error_text="Error"
            page.update()
        else:
            name = txt_name.value
            password = txt_password.value
            page.clean()
            page.add(ft.Text(f"Connected, {name}! Your password is {password}"))

    txt_name = ft.TextField(label="Your Login")
    txt_password = ft.TextField(label="Your password")

    nome = txt_name.value
    password = txt_password.value
    page.add(txt_name, txt_password, ft.ElevatedButton("Connected!", on_click=btn_click))
    page.update()

ft.app(target=main)
cursor.close()
conexao.close()
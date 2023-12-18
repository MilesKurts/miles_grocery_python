import mysql.connector
import flet as ft

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro', 
)

cursor = conexao.cursor()

def verifyLogin(username, password, filepath):
    try:
        password = password+'\n'

        with open(filepath, 'r') as file:
            lines = file.readlines()

            for line in lines:

                fields = line.split(',')

                if(fields[0] ==username and fields[1] == password):
                    return True
    except Exception:
        print(Exception)
    return False

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
    enter_1 = ft.TextField(label="Your name")
    enter_2 = ft.TextField(label="Your password")

    def button_fct(e):
        if not enter_1.value:
            enter_1.error_text = "Please enter your Login name"
            page.update()
        elif not enter_2.value:
            enter_2.error_text = "Please enter your password"
            page.update()
        elif verifyLogin(f"{enter_1.value}",f"{enter_2.value}","data.txt") == True:
            page.clean()
            result = ft.Text("You're in")
            page.add(result)
        else:
            enter_1.error_text = "Error"
            result = ft.Text("You're out")
            page.add(result)


    page.add(title_main, enter_1, enter_2, ft.ElevatedButton("CONNECT", on_click=button_fct))
    page.update()


ft.app(target=main)
cursor.close()
conexao.close()
from flet import *
import flet as ft
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro', 
)

cursor = mydb.cursor()

def main(page:Page):
    page.scroll = "auto"
    nametxt = TextField(label='name')
    password = TextField(label='password')

    edit_nametxt = TextField(label='name')
    edit_passtxt = TextField(label='password')
    edit_id = Text()

    mydt = DataTable(
        columns=[
            DataColumn(Text('id')),
            DataColumn(Text('name')),
            DataColumn(Text('password')),
            DataColumn(Text('actions')),
        ],

        rows=[]
    )
    def deletebtn(e):
        print("you selected id is =", e.control.data['id'])
        try:
            sql = "DELETE FROM login_ WHERE id = %s"
            val = (e.control.data['id'],)
            cursor.execute(sql, val)
            mydb.commit()
            print("deleted")
            mydt.rows.clear()
            load_data()


            page.snack_bar =SnackBar(
                Text("Data delete", size=30),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("Error")

    

    def savedata(e):
        try:
            sql = "UPDATE login_ SET pass_login = %s , name_ = %s where id = %s"
            val = (edit_passtxt.value,edit_nametxt.value, edit_id.value)
            cursor.execute(sql,val)
            mydb.commit()
            print('Ok save')
            dialog.open = False
            page.update()

            edit_nametxt.value = ''
            edit_passtxt.value= ''
            edit_id.value = ''
            mydt.rows.clear()
            load_data()

            page.snack_bar = SnackBar(
                Text("Data saved", size=30),
                bgcolor="green"
            )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("Error")

            page.update()

            page.snack_bar =SnackBar(
                Text("Data edit", size=30),
                bgcolor="green"
            )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("Error edit")

            


    dialog = AlertDialog(
        title=Text("edit data"),
        content=Column([
            edit_nametxt,
            edit_passtxt
        ]),
        actions=[
            TextButton('save',
                       on_click=savedata
                       )
        ]
    )
    def editbtn(e):
        edit_nametxt.value = e.control.data['name_']
        edit_passtxt.value = e.control.data['pass_login']
        edit_id.value = e.control.data['id']
        page.dialog = dialog
        dialog.open = True
        page.update()

    def load_data():
        cursor.execute("SELECT * FROM login_")
        result = cursor.fetchall()

        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['id'])),
                        DataCell(Text(row['name_'])),
                        DataCell(Text(row['pass_login'])),
                        DataCell(
                            Row([
                            IconButton('delete', icon_color="red",
                                           data=row,
                                           on_click=deletebtn
                                           ),
                            IconButton('create', icon_color="red",
                                           data=row,
                                           on_click=editbtn
                                           ),
                            ]),
                )]
                )
            )
                        
            
        page.update()
    
    load_data()

    def addtodb(e):
        try:
            sql = 'INSERT INTO login_ (name_, pass_login) VALUES(%s,%s)'
            val = (nametxt.value,password.value)
            cursor.execute(sql,val)
            mydb.commit()
            print(cursor.rowcount,"You record insert")

            mydt.rows.clear()
            load_data()

            page.snack_bar = SnackBar(
                Text("Data ok", size=30),
                bgcolor="green"
            )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("Error")

        nametxt.value = ''
        password.value= ''
        page.update()

    page.add(
        Column([
            nametxt,
            password,
            ElevatedButton('add to data base',
                on_click=addtodb
            ),
            mydt
        ])
    )

ft.app(target=main)
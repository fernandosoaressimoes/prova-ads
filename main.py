import flet as ft


def main(page: ft.Page):
    page.title = "Meu primeiro app"
    page.add(ft.Text("Olá, Flet!"))


ft.run(main)

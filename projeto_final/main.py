import flet as ft

from solitaire import Solitaire


# ===== Programa principal =====
def main(page: ft.Page):
    solitaire = Solitaire()
    page.add(solitaire)


ft.run(main, assets_dir="assets")

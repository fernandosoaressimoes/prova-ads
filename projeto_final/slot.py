import flet as ft

# ===== Tamanho do slot =====
SLOT_WIDTH = 70
SLOT_HEIGHT = 100


# ===== Slot: Container que guarda uma pilha (pile) de cartas =====
class Slot(ft.Container):
    def __init__(self, top, left):
        super().__init__()
        self.pile = []  # cartas que estão neste slot
        self.width = SLOT_WIDTH
        self.height = SLOT_HEIGHT
        self.left = left
        self.top = top
        self.border = ft.Border.all(1)

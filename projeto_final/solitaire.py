import flet as ft

from slot import Slot
from card import Card

# ===== Tamanho da mesa =====
SOLITAIRE_WIDTH = 1000
SOLITAIRE_HEIGHT = 500

# ===== Imagem de fundo da mesa (arquivo em assets/images) =====
BACKGROUND_IMAGE = "images/fundo_mesa.jpg"


# ===== Solitaire: Stack que cria slots e cartas =====
class Solitaire(ft.Stack):
    def __init__(self):
        super().__init__()
        # ===== Fundo da mesa: primeiro controle, fica atrás de tudo =====
        self.background = ft.Image(
            src=BACKGROUND_IMAGE,
            left=0,
            top=0,
            width=SOLITAIRE_WIDTH,
            height=SOLITAIRE_HEIGHT,
            fit=ft.BoxFit.COVER,
        )
        self.controls = [self.background]
        self.slots = []
        self.cards = []
        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    # ===== Roda logo depois de ser adicionado na página =====
    def did_mount(self):
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    # ===== Cria as cartas =====
    def create_card_deck(self):
        card1 = Card(self, color="GREEN")
        card2 = Card(self, color="YELLOW")
        card3 = Card(self, color="RED")
        self.cards = [card1, card2, card3]

    # ===== Cria os slots =====
    def create_slots(self):
        self.slots.append(Slot(top=0, left=0))
        self.slots.append(Slot(top=0, left=200))
        self.slots.append(Slot(top=0, left=300))
        self.controls.extend(self.slots)
        self.update()

    # ===== Distribui as cartas no primeiro slot =====
    def deal_cards(self):
        self.controls.extend(self.cards)
        for card in self.cards:
            card.place(self.slots[0])
        self.update()
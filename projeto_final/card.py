import flet as ft

# ===== Constantes da carta =====
CARD_WIDTH = 70
CARD_HEIGHT = 100
DROP_PROXIMITY = 20  # distância máxima para "encaixar" no slot
CARD_OFFSET = 20     # deslocamento vertical entre cartas (pilha em leque)

# ===== Imagem de cada carta (arquivos em assets/images) =====
CARD_IMAGES = {
    "GREEN": "images/hacker.jpg",
    "YELLOW": "images/bahiano.jpg",
    "RED": "images/ritual.jpg",
}


# ===== Card: GestureDetector que sabe em qual slot está =====
class Card(ft.GestureDetector):
    def __init__(self, solitaire, color):
        super().__init__()
        self.slot = None
        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5
        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop
        self.left = None
        self.top = None
        self.solitaire = solitaire
        self.color = color
        self.draggable_pile = [self]  # cartas arrastadas junto com esta
        # ===== Carta com imagem; sem imagem, usa só a cor de fundo =====
        image = CARD_IMAGES.get(self.color)
        self.content = ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            bgcolor=self.color.lower(),
            content=ft.Image(
                src=image,
                width=CARD_WIDTH,
                height=CARD_HEIGHT,
                fit=ft.BoxFit.FILL,
            ) if image else None,
        )

    # ===== Pega a carta clicada + todas as que estão abaixo dela =====
    def get_draggable_pile(self):
        """returns list of cards that will be dragged together, starting with the current card"""
        if self.slot is not None:
            self.draggable_pile = self.slot.pile[self.slot.pile.index(self):]
        else:  # slot == None quando a carta ainda vai ser distribuída
            self.draggable_pile = [self]

    # ===== Pilha arrastada fica por cima das outras =====
    def move_on_top(self):
        """Brings draggable card pile to the top of the stack"""
        for card in self.draggable_pile:
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()

    # ===== Voltar pilha para posição original =====
    def bounce_back(self):
        """Returns draggable pile to its original position"""
        for card in self.draggable_pile:
            card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            card.left = card.slot.left
        self.solitaire.update()

    # ===== Colocar pilha no slot (com offset = leque) =====
    def place(self, slot):
        """Place draggable pile to the slot"""
        for card in self.draggable_pile:
            # remove a carta do slot antigo, se existir
            # (antes de calcular o top, para funcionar também no mesmo slot)
            if card.slot is not None:
                card.slot.pile.remove(card)

            card.top = slot.top + len(slot.pile) * CARD_OFFSET
            card.left = slot.left

            # muda o slot da carta e adiciona na pilha nova
            card.slot = slot
            slot.pile.append(card)

        self.solitaire.update()

    # ===== Quando começa a arrastar =====
    def start_drag(self, e: ft.DragStartEvent):
        self.get_draggable_pile()
        self.move_on_top()
        self.solitaire.update()

    # ===== Arrastando: move a pilha inteira =====
    def drag(self, e: ft.DragUpdateEvent):
        for card in self.draggable_pile:
            card.top = (
                max(0, self.top + e.local_delta.y)
                + self.draggable_pile.index(card) * CARD_OFFSET
            )
            card.left = max(0, self.left + e.local_delta.x)
        self.solitaire.update()

    # ===== Soltar: procura slot próximo ou volta =====
    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.slots:
            if (
                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                return

        self.bounce_back()
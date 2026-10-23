# Relatório de Uso de Inteligência Artificial

**Aluno:** Fernando Soares Simões
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)
**Avaliação:** P2 — Prática (Projeto Final: Solitaire em Flet)

## 1. Objetivo deste relatório

Este relatório registra, de forma transparente, como utilizei uma ferramenta de Inteligência Artificial (IA) durante o desenvolvimento do projeto final. A IA foi usada como apoio de consulta, para tirar dúvidas sobre **como colocar imagens no código** e **como organizar melhor o projeto**. A lógica do jogo (cartas, slots, arrastar e soltar) segue a estrutura estudada em aula.

## 2. Consulta 1: como colocar imagens no código

### Dúvida

Eu queria trocar as cartas, que eram apenas retângulos coloridos, por imagens, e também colocar uma imagem de fundo na mesa. Não sabia onde guardar os arquivos nem como o Flet encontra essas imagens.

### O que aprendi com a consulta

1. **Pasta de assets:** as imagens precisam ficar em uma pasta própria (`assets/images`), e o Flet precisa ser informado dessa pasta ao iniciar o programa. Por isso, no `main.py`, o programa é executado com `ft.run(main, assets_dir="assets")`.
2. **Caminho relativo:** depois de definir a pasta `assets`, o caminho da imagem no código é escrito a partir dela, por exemplo `"images/hacker.jpg"`, e não o caminho completo do computador.
3. **Imagem dentro da carta:** no `card.py`, cada carta é um `ft.Container` que recebe um `ft.Image` como conteúdo, com a mesma largura e altura da carta e `fit=ft.BoxFit.FILL` para a imagem preencher a carta inteira.
4. **Dicionário de imagens:** foi sugerido usar um dicionário (`CARD_IMAGES`) ligando cada cor de carta ao seu arquivo de imagem. Assim fica fácil trocar uma imagem sem mexer no resto do código.
5. **Plano B sem imagem:** se uma cor não tiver imagem no dicionário, a carta continua aparecendo só com a cor de fundo (`bgcolor`), evitando erro.
6. **Fundo da mesa:** no `solitaire.py`, a imagem `fundo_mesa.jpg` é adicionada como **primeiro controle** do `Stack`. Como o `Stack` desenha os controles na ordem em que estão na lista, o fundo fica atrás dos slots e das cartas. Foi usado `fit=ft.BoxFit.COVER` para cobrir toda a mesa.

### Imagens usadas no projeto

| Arquivo | Onde é usado | Função |
|---|---|---|
| `hacker.jpg` | `card.py` (carta GREEN) | Imagem da carta verde |
| `bahiano.jpg` | `card.py` (carta YELLOW) | Imagem da carta amarela |
| `ritual.jpg` | `card.py` (carta RED) | Imagem da carta vermelha |
| `fundo_mesa.jpg` | `solitaire.py` | Fundo da mesa do jogo |

## 3. Consulta 2: como ter uma boa organização

### Dúvida

Eu queria saber como deixar o projeto mais organizado e fácil de entender para quem fosse corrigir.

### O que aprendi e apliquei

1. **Um arquivo por responsabilidade:**

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Ponto de entrada: cria a página e adiciona o jogo |
| `solitaire.py` | Classe `Solitaire` (a mesa): cria cartas, slots e distribui as cartas |
| `card.py` | Classe `Card`: aparência da carta e lógica de arrastar e soltar |
| `slot.py` | Classe `Slot`: espaço onde as cartas são empilhadas |
| `assets/images/` | Todas as imagens do projeto |

2. **Constantes no topo do arquivo:** valores como `CARD_WIDTH`, `CARD_HEIGHT`, `CARD_OFFSET`, `DROP_PROXIMITY`, `SOLITAIRE_WIDTH` e `BACKGROUND_IMAGE` ficam no começo de cada arquivo, em letras maiúsculas. Assim, para mudar um tamanho ou uma imagem, basta alterar em um só lugar.
3. **Comentários separando as partes:** usei comentários no padrão `# ===== Título =====` para dividir o código em blocos (constantes, classe, cada método), facilitando a leitura.
4. **Nomes claros:** métodos com nomes que dizem o que fazem, como `create_card_deck`, `create_slots`, `deal_cards`, `place`, `bounce_back` e `move_on_top`.
5. **Imagens separadas do código:** guardar as imagens em `assets/images` deixa a pasta do código limpa e evita misturar arquivos `.py` com arquivos de imagem.

### Estrutura final da pasta

```
projeto_final/
├── assets/
│   └── images/
│       ├── bahiano.jpg
│       ├── fundo_mesa.jpg
│       ├── hacker.jpg
│       └── ritual.jpg
├── card.py
├── main.py
├── slot.py
├── solitaire.py
└── RELATORIO_USO_IA.md
```

## 4. Como a IA foi usada (e como não foi)

| Usei a IA para | Não usei a IA para |
|---|---|
| Entender como o Flet carrega imagens (`assets_dir`) | Substituir o estudo do conteúdo da aula |
| Saber como colocar uma imagem dentro de um `Container` | Copiar um projeto pronto sem entender |
| Saber como colocar o fundo atrás das cartas no `Stack` | Decidir sozinha as regras do jogo |
| Receber sugestões de organização de pastas e arquivos | |
| Melhorar comentários e nomes no código | |

Todas as sugestões foram revisadas, testadas no VS Code e ajustadas por mim antes de serem enviadas ao repositório.

## 5. Conclusão

A IA funcionou como uma ferramenta de consulta, parecida com tirar uma dúvida com um colega ou ler a documentação. Com ela, entendi como o Flet trabalha com imagens (pasta `assets`, caminho relativo, `ft.Image` e ordem dos controles no `Stack`) e como deixar o projeto mais organizado (um arquivo por classe, constantes no topo, comentários e pasta separada para imagens). Esse conhecimento posso reaproveitar em próximos projetos.

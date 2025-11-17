from nicegui import ui
from random import shuffle

# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle
EMOJIS = ['☺️','💢','💯','👁️','😟','🎃','🦅','🇺🇸']  # ← Your task
EMOJIS = EMOJIS * 2 # create 16
shuffle(EMOJIS)

buttons = []
opened = []    # indices of currently flipped cards
matched = []   # indices of solved cards

# TODO 2: Write function to flip non-matching cards back
def reset_pair(i, j):
    buttons[i].text = '❓'
    buttons[j].text = '❓'

# TODO 3: Write click handler
def handle_click(idx):
    if idx in opened or idx in matched:
        return
    
    # flip
    opened.append(idx)
    buttons[idx].text = EMOJIS[idx]

    # wait for second card
    if len(opened) == 2:
        # check for match
        i, j = opened[0], opened[1]
        if EMOJIS[i] == EMOJIS[j]:
            # match
            matched.extend([i, j])

            # win
            if len(matched) == 16:
                ui.notify("You win!") 
        else:
            # not a match
            ui.timer(0.5, lambda: reset_pair(i, j), once=True)
        
        opened.clear()

def restart():
    matched.clear()
    opened.clear()
    shuffle(EMOJIS)
    for i in range(len(buttons)):
        buttons[i].text = '❓'

# Build 4x4 grid
with ui.card():
    ui.label("Memory Game").style("font-size:20px")
    with ui.grid(columns=4):
        # TODO 4: Create 16 buttons
        for i in range(16):
            b = ui.button('❓', on_click=lambda i=i: handle_click(i), color="white")
            buttons.append(b)
    ui.separator()
    ui.button("Restart", on_click=restart, color="orange")


ui.dark_mode().enable()
ui.run(title='Memory Game') 
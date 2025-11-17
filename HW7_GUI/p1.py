from nicegui import ui

def calc_hash():
    text = input_field.value
    h = 0x9E3779B1
    for c in text:
        h = h ^ ord(c)
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF
    h = h ^ len(text)

    hash_label.text = f"Hash value: {h}"

with ui.card().classes("h-65 w-100 self-auto"):
    ui.label("Hashing").style("font-size:20px")
    input_field = ui.input("Text to hash")
    hash_label = ui.label("Hash value: ").classes("font-mono text-lg")
    ui.button("Get Hash", on_click=calc_hash, color="yellow").classes("text-black")

ui.dark_mode().enable()
ui.run(title='Text Hashing')
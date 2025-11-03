from nicegui import ui

ui.label('Wake up, Neo').style("color:green; font-size:20px")

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}!" # fallback for if no input is given for name
    ui.notify(msg) # create a popup

input_field = ui.input("Enter your name")
ui.button("Greet me!", on_click=greet, color="green")

class State:
    count = 0

count_label = ui.label("Count: 0")

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"

# TODO
# Create Reset button which sets the counter to 0

def reset():
    State.count = 0
    count_label.text = f"Count: {State.count}"

ui.button("Add 1", on_click=add_one)
ui.button("Reset", on_click=reset)

ui.run(title="Simple Greeting App") # title
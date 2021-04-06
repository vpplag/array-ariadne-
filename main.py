def on_button_pressed_a():
    global Counter
    basic.show_string("" + (text_list[Counter]))
    Counter += 1
    if Counter >= len(text_list):
        Counter = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

text_list: List[str] = []
Counter = 0
Counter = 0
text_list = ["ARIADNE", "ELENI", "VASSILIS", "ELECTRA"]
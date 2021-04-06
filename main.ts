input.onButtonPressed(Button.A, function () {
    basic.showString("" + (text_list[Counter]))
    Counter += 1
    if (Counter >= text_list.length) {
        Counter = 0
    }
})
let text_list: string[] = []
let Counter = 0
Counter = 0
text_list = ["ARIADNE", "ELENI", "VASSILIS", "ELECTRA"]

radio.set_group(80)
povoleno = 0
counter = 0
number = 0

def on_button_pressed_b():
    global povoleno
    if povoleno == 0:
        povoleno = 1
        basic.show_icon(IconNames.YES)
    elif povoleno == 1:
        povoleno = 0
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a():
    radio.send_value("povoleni", povoleno)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global hlasy
    hlasy.clear()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

hlasy: any = [{"sernumb": 0, "hlas": "0"}]
vote = {"sernumb": 1254, "hlas": "A"}

def on_received_value(hlas, cislo):
    number = cislo
    vote["hlas"] = String.from_char_code(number+65)
radio.on_received_value(on_received_value)
def on_received_value1(serialnumber, sernumb):
    global counter
    for x in hlasy:
        if hlasy[counter]["sernumb"] == sernumb:
            hlasy[counter]["hlas"] = String.from_char_code(number+65)
            counter = 0
            break
        counter += 1
    if counter == len(hlasy):
        vote["sernumb"] = sernumb        
        hlasy.append(vote)
    serial_confirm = sernumb
    radio.send_value("confirm", serial_confirm)
radio.on_received_value(on_received_value1)

console.log_value("hlasy", hlasy)
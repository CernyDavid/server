radio.setGroup(80)
let povoleno = 0
let counter = 0
let number = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (povoleno == 0) {
        povoleno = 1
        basic.showIcon(IconNames.Yes)
    } else if (povoleno == 1) {
        povoleno = 0
        basic.showIcon(IconNames.No)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendValue("povoleni", povoleno)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    _py.py_array_clear(hlasy)
})
let hlasy = [ {
    "sernumb" : 0,
    "hlas" : "0",
}
]
let vote = {
    "sernumb" : 1254,
    "hlas" : "A",
}

radio.onReceivedValue(function on_received_value(hlas: string, cislo: number) {
    let number = cislo
    vote["hlas"] = String.fromCharCode(number + 65)
})
radio.onReceivedValue(function on_received_value1(serialnumber: string, sernumb: number) {
    
    for (let x of hlasy) {
        if (hlasy[counter]["sernumb"] == sernumb) {
            hlasy[counter]["hlas"] = String.fromCharCode(number + 65)
            counter = 0
            break
        }
        
        counter += 1
    }
    if (counter == hlasy.length) {
        vote["sernumb"] = sernumb
        hlasy.push(vote)
    }
    
    let serial_confirm = sernumb
    radio.sendValue("confirm", serial_confirm)
})
console.logValue("hlasy", hlasy)

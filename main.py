radio.set_group(80)
h: any = []
hlasy = [{"sernumb": 1254, "hlas": "A"}, {"sernumb": 8744, "hlas": "B"}]

def on_received_value(hlas, cislo):
    pass
radio.on_received_value(on_received_value)
def on_received_value1(serialnumber, sernumb):
    for x in hlasy:
        pass
radio.on_received_value(on_received_value1)
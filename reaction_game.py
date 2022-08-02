import machine
import utime
import urandom

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN)

def button_press(pin):
    button.irq(handler=None)
    reaction_time = utime.ticks_diff(utime.ticks_ms(), timer_light_off)
    print("Reaksjonstiden din er " + str(reaction_time) + " millisekunder!")
    if reaction_time <= 250:
        print("Du er raskere enn gjennomsnittsmennesket!")

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
timer_light_off = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)

#https://docs.sunfounder.com/projects/thales-kit/en/latest/reaction_game.html

import machine
import utime
import urandom

led = machine.Pin(15, machine.Pin.OUT)
left_button = machine.Pin(14, machine.Pin.IN)
right_button = machine.Pin(16, machine.Pin.IN)

def button_press(pin):
    left_button.irq(handler=None)
    right_button.irq(handler=None)
    rection_time = utime.ticks_diff(utime.ticks_ms(), timer_light_off)
    if pin == left_button:
        print("Nummer 1 vant!!")
    elif pin == right_button:
        print("Nummer 2 vant!!!")
    print("Reaksjonstiden din er " + str(rection_time) + " millisekunder!")

print(" - - - Spillet er igang - - - ")


led.value(1)
utime.sleep(urandom.uniform(5, 20))
led.value(0)
timer_light_off = utime.ticks_ms()
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)

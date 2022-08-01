import machine
import utime

potentiometer = machine.ADC(28)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

button = machine.Pin(14, machine.Pin.IN)

while True:
    value=potentiometer.read_u16()
    print(value)
    led.duty_u16(value)
    utime.sleep_ms(200)

    if button.value() == 0:
        print("-- 0 -- ")
        utime.sleep(2)
   
    

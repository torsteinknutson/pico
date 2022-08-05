from lcd1602 import LCD
import utime

while True:
        
    lcd = LCD()
    string = "  WHEN I SEE CATS \n"
    lcd.message(string)
    utime.sleep(5)
    lcd.clear()
    string = "  \n  I CLICK!  "
    lcd.message(string)
    utime.sleep(1.5)
    lcd.clear()


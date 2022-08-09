from lcd1602 import LCD
import utime

while True:
        
    lcd = LCD()
    string = " WHEN*I*SEE*CATS\n"
    lcd.message(string)
    utime.sleep(2.9)
    lcd.clear()
    string = "  \n    I*CLICK!"
    lcd.message(string)
    utime.sleep(2.99)
    lcd.clear()
    
    
    string = "X"
    
    while True:
    
        if len(string) < 16:
            string = " "+string
            lcd.message(string)
            utime.sleep(0.1)
            lcd.clear()
            
                    
        else:
            break
              


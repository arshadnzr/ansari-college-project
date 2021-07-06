import RPi.GPIO as GPIO 
import lcddriver
from time import * 

lcd = lcddriver.lcd()
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) 
lcd.lcd_display_string("		PROJECT", 1)
lcd.lcd_display_string("An Electronic Assistant", 2)
lcd.lcd_display_string("	For Deaf-Mute", 3)
sleep(3)
lcd.lcd_clear()

while True:
   button_state=GPIO.input(10) 
   if(button_state==0):
        lcd.lcd_clear()
        lcd.lcd_display_string("	Gesture mode", 2)
        lcd.lcd_display_string("		Activated", 3)
        sleep(2)
        lcd.lcd_clear()
        import fun_util fun_util.recognize()
   else:
        lcd.lcd_clear()
   	    lcd.lcd_display_string("	Speech mode", 2)
        lcd.lcd_display_string("		Activated", 3)
        sleep(2)
        lcd.lcd_clear() 
        import speech speech.rec()
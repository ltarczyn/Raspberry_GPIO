'''
Program sterujący pracą oswietlenia zewnętrzengo domu oraz garażu

'''

import RPi.GPIO as GPIO
import time
"ustawienie numeracji GPIO"
GPIO.setmode(GPIO.BCM)
"Ustawienie pinów WE/WY"
GPIO.setup(0, GPIO.OUT)  # ustawienie gpio0 jako wyjscie
GPIO.setup(1, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # ustawienie gpio 4 na pin WEJSCIOWY
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)
"GPIO.wait_for_edge(26, GPIO.FALLING) #czekamy na wciśnięcie przycisku który jest podpiety do pinu 26. Po naciśnięciu przechodzimy do dalszej częsci programu"


while True:
    GPIO.output(0, GPIO.HIGH)
    GPIO.output(1, GPIO.HIGH)

    if GPIO.wait_for_edge(4, GPIO.FALLING):
        GPIO.output(0, GPIO.LOW)
        print("wysyłanie sygnału do odbiornika świateł w domu")
        time.sleep(2)
        GPIO.output(0, GPIO.HIGH)
        print ("włączenie świateł na garażu")
        GPIO.output(1, GPIO.LOW)

        """print (f"wejscie 4 {GPIO.input(4)}, wejscie 14 {GPIO.input(17)}")"""
        time.sleep(5)






import RPi.GPIO as GPIO
from gpiozero import TonalBuzzer, Button
from gpiozero.tones import Tone
import time
import sys

#shift register pins
dataPin = 16
latchPin = 20
clockPin = 21

#buzzer and button setup
buzzer = TonalBuzzer(27)
button = Button(13)


score = 0
speed = 0.8


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    

def shiftOut(dPin, cPin, val):
    for i in range(0,7):
        GPIO.output(cPin, GPIO.LOW)
        GPIO.output(dPin, (0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin, GPIO.HIGH)
        
def lossSound():
    global buzzer 
    
    buzzer.play(Tone("A4"))
    time.sleep(0.4)
    buzzer.stop()
    time.sleep(0.3)
    buzzer.play(Tone("G#4"))
    time.sleep(0.5)
    buzzer.stop()
    time.sleep(0.2)
    buzzer.play(Tone("G4"))
    time.sleep(1.6)
    buzzer.stop()

def evalGame(activeLight):
    global score 
    global speed
    global buzzer
    if activeLight == 0x08:
        buzzer.play(Tone("C5"))
        time.sleep(0.1)
        buzzer.stop()
        score += 1
        print("Current Score: " + str(score))
        if speed > 0.1:
            speed -= 0.05
        else:
            speed *= 0.9
    else:
        print("Game Over")
        lossSound()
        print("Final score: " + str(score))
        response = input("Try again?")
        if str(response) == "y":
            return "continue"
        else:
            return "quit"
        
         
        
        


    
    

def gameLoop():
    global speed
    global buzzer
    global activeLight
    playing = True
    
    activeLight = 0x01
    print ('Lets begin')
    while playing:
        for i in range(0,6):
            buzzer.play(Tone("C4"))
            time.sleep(0.05)
            buzzer.stop()
            time.sleep(speed)
            GPIO.output(latchPin, GPIO.LOW)
            shiftOut(dataPin, clockPin, activeLight)
            GPIO.output(latchPin, GPIO.HIGH)
            #print(activeLight)
            if button.is_pressed:
                cont = evalGame(activeLight)
                if cont == "quit":
                    quit()
                elif cont == "continue":
                    speed = 0.8
                    score = 0
                    gameLoop()
                    
            activeLight<<=1
            
        for i in range (0,6):
            buzzer.play(Tone("C4"))
            time.sleep(0.05)
            buzzer.stop()
            time.sleep(speed)
            GPIO.output(latchPin, GPIO.LOW)
            shiftOut(dataPin, clockPin, activeLight)
            GPIO.output(latchPin, GPIO.HIGH)
            #print(activeLight)
            if button.is_pressed:
                evalGame(activeLight)
            activeLight>>=1
                        
        

if __name__ == '__main__': 
    setup()
    
    try:
       gameLoop()
       
    except KeyboardInterrupt:
        GPIO.cleanup()

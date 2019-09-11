import time
import os
import board
import digitalio

button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

#button2 = digitalio.DigitalInOut(board.D24)
#button2.direction = digitalio.Direction.INPUT
#button2.pull = digitalio.Pull.UP

#button3 = digitalio.DigitalInOut(board.D25)
#button3.direction = digitalio.Direction.INPUT
#button3.pull = digitalio.Pull.UP

currentDate = time.localtime()
print("press a button!")

while True:
    
    if not button1.value:
        os.system('echo "I, , , Today is " | festival --tts')
        os.system('currentDate | festival --tts')
        os.system('festival --tts events.txt')

#    if not button2.value:
#        os.system('echo "I, , , Some rescue!" | festival --tts')

#    if not button3.value:
#        os.system('echo "I, , , I find your lack of faith disturbing." | festival --tts')

    time.sleep(0.1)

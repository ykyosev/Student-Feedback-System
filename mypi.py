#mypi.py
import RPi.GPIO as GPIO
from time import sleep
import csv
import datetime
import os.path
import requests

GPIO.setmode(GPIO.BCM)
sleepTime = .1
#GPIO of BAD Button and LED
lightPin1 = 4
buttonPin1 = 17
GPIO.setup(lightPin1, GPIO.OUT)
GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin1, False)
#GPIO of OK Button and LED
lightPin2 = 27
buttonPin2 = 22
GPIO.setup(lightPin2, GPIO.OUT)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin2, False)
#GPIO of GREAT Button and LED
lightPin3 = 23
buttonPin3 = 24
GPIO.setup(lightPin3, GPIO.OUT)
GPIO.setup(buttonPin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin3, False)


def badBtn(a):
      button_time = datetime.datetime.now()
      data.writerow([button_time,"1","0","0"])
      csv_file.flush()
      print(button_time, "Bad")
      sending1 = requests.get("http://192.168.1.5:3030/add?location=itl01&answer=bad")
      
def okBtn(a):
      button_time = datetime.datetime.now()
      data.writerow([button_time,"0","1","0"])
      csv_file.flush()
      print(button_time, "Ok")
      sending2 = requests.get("http://192.168.1.5:3030/add?location=itl01&answer=ok")
      
def greatBtn(a):
      button_time = datetime.datetime.now()
      data.writerow([button_time,"0","0","1"])
      csv_file.flush()
      print(button_time, "Great")
      sending3 = requests.get("http://192.168.1.5:3030/add?location=itl01&answer=great")

# check if file data.csv exists 
file_exists = os.path.exists("/home/pi/Desktop/data.csv")
with open('data.csv','a') as csv_file:
      data = csv.writer(csv_file)
      headers = ['Time', 'Bad','Ok','Great']
      writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n', fieldnames = headers)

      # if True, do not put headings again as they were already added at file creation
      if not file_exists:
            data.writerow(['Time', 'Bad','Ok','Great'])
            
    # Now loop creating new entry on the csv file every time a button is pressed
      try:
          GPIO.add_event_detect(17, GPIO.RISING, callback = badBtn, bouncetime= 400)
          GPIO.add_event_detect(22, GPIO.RISING, callback = okBtn, bouncetime= 400)
          GPIO.add_event_detect(24, GPIO.RISING, callback = greatBtn, bouncetime= 400)
          while True:
            GPIO.output(lightPin1, not GPIO.input(buttonPin1))
            GPIO.output(lightPin2, not GPIO.input(buttonPin2))
            GPIO.output(lightPin3, not GPIO.input(buttonPin3))
            sleep(.1)
            
            input_bad = 0
            input_ok = 0
            input_great = 0
            if input_bad == True:
                  GPIO.output (17, GPIO.LOW)                       
            elif input_ok == True:
                  GPIO.output(22, GPIO.LOW)
            elif input_great == True:
                  GPIO.output(24, GPIO.LOW)
                                
      finally:
        GPIO.output(lightPin1, False)
        GPIO.output(lightPin2, False)
        GPIO.output(lightPin3, False)
        GPIO.cleanup()

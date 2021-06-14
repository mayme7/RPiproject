  import RPi.GPIO as GPIO
  import time
  
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)

  led_pin1 = 12
  led_pin2 = 16
  
  GPIO.setup(led_pin1, GPIO.OUT)
  GPIO.setup(led_pin2, GPIO.OUT)
  
  ##단계(1~10)를 넣어 LED 밝기를 조절
  def setLight(light, p):
      p.ChangeDutyCycle(light)
      
  try:
      p1 = GPIO.PWM(led_pin1, 100)
      p2 = GPIO.PWM(led_pin2, 100)
      p1.start(0)
      p2.start(0)
  
      while True :
          # 첫번째 LED 점점 밝아지게
          for i in range(10):
              GPIO.output(led_pin1, True)
              p1.ChangeDutyCycle(i*10)
              setLight(i * 10, p1)
              time.sleep(0.5)
              
           # 두번째 LED 점점 어두워지게
          for j in range(10, -1, -1):
              p2.start(100)
              GPIO.output(led_pin2, True)
              p2.ChangeDutyCycle(j*10)
              setLight(j * 10, p2)
              time.sleep(0.5)  
          
  except KeyboardInterrupt:
      pass
  finally:
      GPIO.cleanup()

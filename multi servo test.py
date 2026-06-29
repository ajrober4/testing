from gpiozero import AngularServo
from time import sleep

muscle = AngularServo(18,min_angle=0,max_angle=180,min_pulse_width=0.00065,max_pulse_width=0.0025)
base = AngularServo(14,min_angle=0,max_angle=180,min_pulse_width=0.00065,max_pulse_width=0.0025)
hrz = AngularServo(15,min_angle=0,max_angle=180,min_pulse_width=0.0005,max_pulse_width=0.0025)

while True:
    
    muscle.angle = 0
    print(muscle.angle)
    sleep(1)
    muscle.angle = 180
    print(muscle.angle)
    
    sleep(3)

    base.angle = 0
    print(base.angle)
    sleep(1)
    base.angle = 180
    print(base.angle)
    
    sleep(3)

    hrz.angle = 0
    print(hrz.angle)
    sleep(1)
    hrz.angle = 180
    print(hrz.angle)
    
    sleep(3)
#hrz = AngularServo(15,min_angle=-90,max_angle=90,min_pulse_width=0.0005,max_pulse_width=0.0025)
#base = AngularServo(14,min_angle=-90,max_angle=90,min_pulse_width=0.0005,max_pulse_width=0.0025)
   
    #base.angle = 0
    #base.angle = 90
    #base.angle = 0
    #print("Base Servo to wave")
    
    #sleep(2)
    
    #muscle.angle = 0
    #muscle.angle = 90
    #muscle.angle = 0
    #print("muscle Servo to wave")
    


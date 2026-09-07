from gpiozero import Motor
import time

# Left motor: ENA=17, IN1=27, IN2=22
# Right motor: ENB=25, IN3=23, IN4=24
left_motor = Motor(forward=27, backward=22, enable=17)
right_motor = Motor(forward=23, backward=24, enable=25)

def forward(speed=0.6):
    left_motor.forward(speed)
    right_motor.forward(speed)

def backward(speed=0.6):
    left_motor.backward(speed)
    right_motor.backward(speed)

def turn_left(speed=0.6):
    left_motor.backward(speed)
    right_motor.forward(speed)

def turn_right(speed=0.6):
    left_motor.forward(speed)
    right_motor.backward(speed)

def stop():
    left_motor.stop()
    right_motor.stop()

if __name__ == '__main__':
    print("Forward")
    forward()
    time.sleep(2)
    stop()
    time.sleep(1)

    print("Turn left")
    turn_left()
    time.sleep(1)
    stop()
    time.sleep(1)

    print("Turn right")
    turn_right()
    time.sleep(1)
    stop()

    print("Backward")
    backward()
    time.sleep(2)
    stop()
    print("Done")

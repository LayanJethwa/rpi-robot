from gpiozero import Robot, Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time

robot_pins = PiGPIOFactory(host="10.7.0.94")
robot = Robot(left=(23,22),right=(17,18), pin_factory=robot_pins)
forward = Button(21)
left = Button(13)
right = Button(17)
backward = Button(4)

forward.when_pressed = robot.forward
forward.when_released = robot.stop
left.when_pressed = robot.left
left.when_released = robot.stop
right.when_pressed = robot.right
right.when_released = robot.stop
backward.when_pressed = robot.backward
backward.when_released = robot.stop

def on_button_pressed_a():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(5000)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)

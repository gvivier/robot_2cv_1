Dist_0 = 0
dist_180 = 0
Distance = 0
pins.servo_write_pin(AnalogPin.P2, 90)

def on_forever():
    global Distance, dist_180, Dist_0
    Distance = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)
    basic.show_number(Distance)
    if Distance < 15:
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
            kitronik_klip_motor.MotorDirection.REVERSE,
            50)
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
            kitronik_klip_motor.MotorDirection.REVERSE,
            50)
        basic.pause(1000)
        kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
        kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
        basic.pause(500)
        pins.servo_write_pin(AnalogPin.P2, 180)
        basic.pause(500)
        dist_180 = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)
        basic.pause(500)
        pins.servo_write_pin(AnalogPin.P2, 0)
        basic.pause(500)
        Dist_0 = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)
        basic.pause(500)
        if Dist_0 < dist_180:
            kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
                kitronik_klip_motor.MotorDirection.FORWARD,
                80)
            basic.pause(1000)
            kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
        else:
            kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
                kitronik_klip_motor.MotorDirection.FORWARD,
                80)
            basic.pause(1000)
            kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
        basic.show_icon(IconNames.NO)
    else:
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
            kitronik_klip_motor.MotorDirection.FORWARD,
            80)
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
            kitronik_klip_motor.MotorDirection.FORWARD,
            80)
        basic.show_icon(IconNames.YES)
        basic.pause(1000)
basic.forever(on_forever)

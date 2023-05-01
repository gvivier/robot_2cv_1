Dist_30 = 0
dist_150 = 0
Distance = 0
pins.servo_write_pin(AnalogPin.P2, 90)

def on_forever():
    global Distance, dist_150, Dist_30
    Distance = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)
    if Distance < 15:
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
            kitronik_klip_motor.MotorDirection.REVERSE,
            30)
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
            kitronik_klip_motor.MotorDirection.REVERSE,
            30)
        basic.pause(1000)
        kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
        kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
        basic.pause(500)
        pins.servo_write_pin(AnalogPin.P2, 150)
        basic.pause(500)
        dist_150 = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)
        basic.pause(500)
        pins.servo_write_pin(AnalogPin.P2, 30)
        basic.pause(500)
        Dist_30 = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)
        basic.pause(500)
        pins.servo_write_pin(AnalogPin.P2, 90)
        if Dist_30 < dist_150:
            kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
                kitronik_klip_motor.MotorDirection.FORWARD,
                50)
            basic.pause(500)
            kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
        else:
            kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
                kitronik_klip_motor.MotorDirection.FORWARD,
                50)
            basic.pause(500)
            kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    else:
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
            kitronik_klip_motor.MotorDirection.FORWARD,
            50)
        kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
            kitronik_klip_motor.MotorDirection.FORWARD,
            50)
        basic.pause(1000)
basic.forever(on_forever)

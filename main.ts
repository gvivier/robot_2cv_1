let Dist_0 = 0
let dist_180 = 0
let Distance = 0
pins.servoWritePin(AnalogPin.P2, 90)
basic.forever(function () {
    Distance = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P0,
    PingUnit.Centimeters
    )
    if (Distance < 15) {
        kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Reverse, 30)
        kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Reverse, 30)
        basic.pause(1000)
        kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor1)
        kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor2)
        basic.pause(500)
        pins.servoWritePin(AnalogPin.P2, 180)
        basic.pause(500)
        dist_180 = sonar.ping(
        DigitalPin.P1,
        DigitalPin.P0,
        PingUnit.Centimeters
        )
        basic.pause(500)
        pins.servoWritePin(AnalogPin.P2, 0)
        basic.pause(500)
        Dist_0 = sonar.ping(
        DigitalPin.P1,
        DigitalPin.P0,
        PingUnit.Centimeters
        )
        basic.pause(500)
        pins.servoWritePin(AnalogPin.P2, 90)
        if (Dist_0 < dist_180) {
            kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 30)
            basic.pause(1000)
            kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor2)
        } else {
            kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 30)
            basic.pause(1000)
            kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor1)
        }
    } else {
        kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 50)
        kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 50)
        basic.pause(1000)
    }
})

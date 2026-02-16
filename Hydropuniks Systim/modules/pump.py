class Pump:
    def __init__(self, serial_manager):
        self.serial = serial_manager
        self.state = 0

    def turn_on(self):
        self.serial.send("PUMP_ON")
        self.state = 1

    def turn_off(self):
        self.serial.send("PUMP_OFF")
        self.state = 0

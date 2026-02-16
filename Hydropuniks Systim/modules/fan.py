class Fan:
    def __init__(self, serial_manager):
        self.serial = serial_manager
        self.state = 0

    def turn_on(self):
        self.serial.send("FAN_ON")
        self.state = 1

    def turn_off(self):
        self.serial.send("FAN_OFF")
        self.state = 0

    def auto_mode(self):
        self.serial.send("FAN_AUTO")

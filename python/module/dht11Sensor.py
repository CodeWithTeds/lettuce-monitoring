class DHT11Sensor:
    def __init__(self):
        self.temperature = "--"
        self.humidity = "--"

    def update(self, data):
        if "TEMP" in data:
            self.temperature = data["TEMP"]
        if "HUM" in data:
            self.humidity = data["HUM"]

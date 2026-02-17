class PHSensor:
    def __init__(self):
        self.value = "--"

    def update(self, data):
        if "PH" in data:
            self.value = data["PH"]

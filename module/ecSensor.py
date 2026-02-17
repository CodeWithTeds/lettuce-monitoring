class ECSensor:
    def __init__(self):
        self.value = "--"

    def update(self, data):
        if "TDS" in data:
            self.value = data["TDS"]

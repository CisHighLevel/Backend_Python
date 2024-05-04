class Data:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    def to_dict(self):
        return {
            "time": self.time,
            "value": self.value,
        }
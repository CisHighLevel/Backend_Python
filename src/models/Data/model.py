class Data:
    def __init__(self, string, value):
        self.string = string
        self.value = value

    def to_dict(self):
        return {
            "string": self.string,
            "value": self.value,
        }
class QRecord:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.id = 0

    def generate(self):
        self.id += 1
        return [field.generate() for field in self.fields]

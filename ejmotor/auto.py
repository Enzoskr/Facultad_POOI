
class Auto:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def get_marca(self):
        return self.marca
    
    def get_tipo_motor(self):
        return self.motor.get_tipo()


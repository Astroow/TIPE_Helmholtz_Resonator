import math

C0 = 340


class Resonator:
    def __init__(self, surface: float, length: float, volume: float):
        self.surface = surface
        self.length = length
        self.volume = volume

        self.frequency = C0/(2*math.pi)*math.sqrt(self.surface / self.length * self.volume)


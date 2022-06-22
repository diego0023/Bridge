from divice import Divice


class Radio(Divice):

    def __init__(self) -> None:
        self.state: bool = False
        self.volume: int = 50
        self.stations: list[float] = [90.1, 90.3, 90.5, 90.7, 90.9, 91.0]
        self.selectStation: int = 0

    def is_enabled(self):
        return self.state

    def enabled(self):
        self.state = True

    def disable(self):
        self.state = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        if 0 < percent < 100:
            self.volume = percent
        else:
            print("Limite de volumen alcansado")

    def get_channel(self):
        return self.selectStation

    def get_list(self):
        return self.stations

    def set_channel(self, channel):
        if channel > len(self.stations):
            channel = len(self.stations)
        
        self.selectStation = channel
        print(f"Frecuencia: {self.stations[self.selectStation]}")

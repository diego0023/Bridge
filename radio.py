from divice import Divice


class Radio(Divice):
    def __init__(self) -> None:
        self.state: bool = False
        self.volume: int = 50
        self.stations: list[float] = [90.1, 90.3, 90.5 , 90.7, 90.9, 91.0]
        self.selectStation:int = 0

    def is_enabled(self):
        return self.state

    def enabled(self):
        self.state = True

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.selectStation

    def set_channel(self, channel):
        if channel > self.stations.count():
            channel = self.stations.count()
        
        self.selectStation = channel

    

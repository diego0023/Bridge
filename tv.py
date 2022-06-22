from divice import Divice


class TV(Divice):
    def __init__(self):
        self.state: bool = False
        self.volume: int = 50
        self.channel: int = 0

    def is_enabled(self):
        return self.state

    def enabled(self):
        self.state = True

    def disable(self):
        self.state = False

    def set_volume(self, percent):
        if 0 < percent < 100:
            self.volume = percent
        else:
            print("Limite de volumen alcansado")

    def set_channel(self, channel):
        self.channel = channel
        print(f"Canal: {self.channel}")

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

from divice import Divice


class SmartTv(Divice):
    def __init__(self):
        self.state: bool = False
        self.volume: int = 50
        self.channel: str = "Home"
        self.servicios: list[str] = ["Netflix","HBO Max", "Amazon Prime", "YouTube", "Disney Plus"]
        self.select_service = 0
    
    def is_enabled(self): return self.state

    def enabled(self): 
        self.state = True

    def disable(self): 
        self.state = False

    def set_volume(self, percent):
        self.volume = percent

    def set_channel(self, channel):
        if channel > self.servicios.count():
            channel = self.servicios.count()
        
        self.select_service = channel
        print(f"Ahora viendo  {self.servicios[channel]}")

    def get_channel(self):
        return self.servicios[self.select_service]

    def get_volume(self):
        return self.volume

from divice import Divice


class Remote:
    def __init__(self, type) -> None:
        self.divice: Divice = type
    
    def togglepower(self):
        if self.divice.is_enabled():
            self.divice.disable()
        else: 
            self.divice.enabled()
            
        print(f"Estado: {self.divice.is_enabled()}")
    
    def volume_down(self):
        self.divice.set_volume(self.divice.get_volume()-1)
        print(f"Volumen: {self.divice.get_volume()}")
    
    def volume_up(self):
        self.divice.set_volume(self.divice.get_volume() + 1)
        print(f"Volumen: {self.divice.get_volume()}")

    def channel_up(self):
        self.divice.set_channel(self.divice.get_channel() + 1)
        print(f"Canal: {self.divice.get_channel()}")
    
    def channel_down(self):
        self.divice.set_channel(self.divice.get_channel() - 1)
        print(f"Canal: {self.divice.get_channel()}")
        
    


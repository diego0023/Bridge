from remote import  Remote


class AdvanceRemote(Remote):
    def __init__(self, type) -> None:
        super().__init__(type)

    def mute(self):
        self.divice.set_volume(0)
        print("Dispositivo muteado")

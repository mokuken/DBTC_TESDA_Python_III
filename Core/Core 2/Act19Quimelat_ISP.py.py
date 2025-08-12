class Camera:
    def take_photo(self):
        pass
 
class MusicPlayer:
    def play_music(self, song):
        pass

class GPS:
    def navigate(self, destination):
        pass

class Smartphone(Camera, MusicPlayer, GPS):
    def take_photo(self):
        print("taking a photo...")

    def play_music(self, song):
        print("Playing song:", song)

    def navigate(self, destination):
        print("Navigating to:", destination)


class MP3Player(MusicPlayer):
    def play_music(self, song):
        print("Playing song:", song)


# Calling the SocialMediaApp Methods
phone = Smartphone()
phone.take_photo()
phone.play_music("The Shape of You")
phone.navigate("Manila")

# Calling the ChatOnlyApp Methods
mp3Player = MP3Player()
mp3Player.play_music("Blinding the lights")
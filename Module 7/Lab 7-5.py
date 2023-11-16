# Write your MoviePlayer class here
class MoviePlayer:
    firmware_version = 1.0

    def __init__(self):
        self.firmware_version = MoviePlayer.firmware_version
        self._movie_list = ["Frozen", "Finding Nemo", "Toy Story"]
        
    def play(self):
        self.current_movie = self._movie_list[0]

    def list_movies(self):
        return self._movie_list

    def update_firmware(self, version):
        if self.firmware_version < version:
            self.firmware_version = version
        return self.firmware_version

# The code below is used to test your class
if __name__ == '__main__':
    player = MoviePlayer()
    print("Movies currently on device:", player.list_movies())

    player.update_firmware(2.0)
    print("Updated player firmware version to", player.firmware_version)

    player.play()
    print("Currently playing", f"'{player.current_movie}'")


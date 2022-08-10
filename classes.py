class Television:
    """
    A class representing actions to operate a Television (typically with a remote)
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a television object.
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__isOn = False


    def power(self) -> None:
        """
        Method to turn the TV on/off.
        """
        if not self.__isOn:
            self.__isOn = True
        elif self.__isOn:
            self.__isOn = False


    def channel_up(self) -> None:
        """
        Method to adjust the TV channel by incrementing its value.
        """
        if self.__isOn:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1


    def channel_down(self) -> None:
        """
        Method to adjust the TV channel by decrementing its value.
        """
        if self.__isOn:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1


    def volume_up(self) -> None:
        """
        Method to adjust the TV volume by incrementing its value.
        """
        if self.__isOn:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1


    def volume_down(self) -> None:
        """
        Method to adjust the TV volume by decrementing its value.
        """
        if self.__isOn:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1


    def __str__(self) -> str:
        """
        Method to return the TV status using the format shown in the comments of Labmain.py.
        """
        return f'TV status: Is on = {self.__isOn}, Channel = {self.__channel}, Volume = {self.__volume}'

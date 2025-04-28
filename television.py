class Television:
    """
    Class details and permanent values for television
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to set default values for television
        """
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn television on or off
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to mute television
        """
        if self.__status:
            self.__muted = True

    def channel_up(self) -> None:
        """
        Method to change the channel on the television positively
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to change the channel on the television negatively
        """
        if self.__status:
            if self.__channel > Television.MIN_VOLUME:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to turn the television volume up
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to turn the television volume down
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method to show the setting of the television
        :return: Returns current television settings
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        if self.__status:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'



class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        self.minute = minute % 60
        self.hour = (hour + (minute // 60)) % 24

    def __repr__(self) -> str:
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> "Clock":
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> "Clock":
        return self.__add__(-minutes)

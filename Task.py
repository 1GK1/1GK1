class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        if not (isinstance(hours, int) \
                and isinstance(minutes, int) \
                and isinstance(seconds, int)):
            raise TypeError('Enter integers to create TimeInterval object')

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            total_seconds = (self.hours + other.hours) * 3600 \
                            + (self.minutes + other.minutes) * 60 \
                            + (self.seconds + other.seconds)

        if isinstance(other, int):
            total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + other

        new_hours = total_seconds // 3600
        new_minutes = (total_seconds % 3600) // 60
        new_seconds = total_seconds % 60
        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __sub__(self, other):
        total_seconds = (self.hours - other.hours) * 3600 \
                        + (self.minutes - other.minutes) * 60 \
                        + (self.seconds - other.seconds)
        new_hours = total_seconds // 3600
        new_minutes = (total_seconds % 3600) // 60
        new_seconds = total_seconds % 60
        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __mul__(self, other):
        if isinstance(other, int):
            new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other
            new_hours = new_time // 3600
            new_minutes = (new_time % 3600) // 60
            new_seconds = new_time % 60
            print(f'{new_hours}:{new_minutes}:{new_seconds}')
            return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
        else:
            raise TypeError('Can only multiply TimeInterval by integer!')

    def __str__(self):
        self.hours = str(self.hours)
        self.minutes = str(self.minutes)
        self.seconds = str(self.seconds)

        if len(self.hours) == 1:
            self.hours = '0' + self.hours
        if len(self.minutes) == 1:
            self.minutes = '0' + self.minutes
        if len(self.seconds) == 1:
            self.seconds = '0' + self.seconds

        return f'{self.hours}:{self.minutes}:{self.seconds}'


fti = TimeInterval(hours=21, minutes=58, seconds=50)
sti = TimeInterval(hours=1, minutes=45, seconds=22)
example = TimeInterval(hours=1, minutes=1, seconds=8)
sec = 10

print(fti + sec)

# print(fti + sti)
# print(fti + sec)
# print(example)
# print(fti - sti)
# print(fti * 2)

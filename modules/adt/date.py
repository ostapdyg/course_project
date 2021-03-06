class Date:
    """
    A class to represent the time of an event
    """

    @classmethod
    def date_from_str(cls, s):
        """
        Creates a Date object from a string
        :param s: string in a format yyyymmddThhmmssZ
        (year+month+day+T+hour+minute+second+Z)
        :return: a Date object
        """
        try:
            year = int(s[:4])
            month = int(s[4:6])
            day = int(s[6:8])
            s = s.split('T')[1]
            hour = int(s[:2])
            minute = int(s[2:4])
            second = int(s[4:6])
            return cls(year, month, day, hour, minute, second)
        except ValueError:
            raise ValueError('Invalid date format')

    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __eq__(self, other):
        return (self.year == other.year)and \
               (self.month == other.month) and \
               (self.day == other.day) and \
               (self.hour == other.hour) and \
               (self.minute == other.minute) and \
               (self.second == other.second)

    def __gt__(self, other):
        return (self.year > other.year) or \
               (self.month > other.month) or \
               (self.day > other.day) or \
               (self.hour > other.hour) or \
               (self.minute > other.minute) or \
               (self.second > other.second)

    def __lt__(self, other):
        return (self.year < other.year) or \
               (self.month < other.month) or \
               (self.day < other.day) or \
               (self.hour < other.hour) or \
               (self.minute < other.minute) or \
               (self.second < other.second)

    def __ge__(self, other):
        return (self.year <= other.year) or \
               (self.month <= other.month) or \
               (self.day <= other.day) or \
               (self.hour <= other.hour) or \
               (self.minute <= other.minute) or \
               (self.second <= other.second)

    def same_date(self, other):
        return (self.year == other.year) and \
               (self.month == other.month) and \
               (self.day == other.day)

    def __str__(self):
        return '{0}.{1}.{2},{3}:{4}:{5}'.format(self.day,
                                                 self.month,
                                                 self.year,
                                                 self.hour,
                                                 self.minute,
                                                 self.second)

    def file_str(self):
        """
        Return a string representation of a date in format yyyymmddThhmmssZ
        :return:str
        """
        return '{0:4}{1:2}{2:2}T{3:2}{4:2}{5:}Z'.format(self.year,
                                                 self.month,
                                                 self.day,
                                                 self.hour,
                                                 self.minute,
                                                 self.second).replace(' ', '0')


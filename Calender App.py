class Day:
    positionInYear = 0
    event = ""
    def __init__(self, positionInYear, eventname):
        self.positionInYear = positionInYear
        self.eventname = eventname

class Birthday(Day):
    age = 0
    def __init__(self,positionInYear, event, age):
        super().__init__(positionInYear, event)
        self.age = age


class Calendar():
    days = []

    def add_event(self, day, event):
        self.days.append(Day(daynumber, eventname))
    


c = Calendar
c.add_event(360, "Christmas")

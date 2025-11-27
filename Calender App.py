class Day: 
    positionInYear = 0
    event = ""
    def __init__(self, positionInYear, event):
        self.positionInYear = positionInYear
        self.event = event
 
class BirthDay(Day):
    age = 0
    def __init__(self,positionInYear,event,age):
        super().__init__(positionInYear,event)
        self.age = age
 
class BankHoliday(Day):
    def __init__(self,positionInYear):
        super().__init__(positionInYear,"Bank Holiday")
 
class Calendar:
    days = []
    def __init__(self):
        self.days = []
    def add_event(self,daynumber,eventname):
        self.days.append(Day(daynumber,eventname))
    def add_birthday(self,daynumber,age):
        self.days.append(BirthDay(daynumber,"Birthday",age))
    def add_bank_hol(self,daynumber):
        self.days.append(BankHoliday(daynumber))
 
c = Calendar()
c.add_event(360, "Christmas")
c.add_event(1, "New Year's")
c.add_birthday(20,30)
c.add_bank_hol(5)
c.add_event(365, "New Year's Eve")
c.add_event(361, "Boxing Day")
 
for day in c.days:
    print(f"The {day.positionInYear}th day of the year is {day.event}")

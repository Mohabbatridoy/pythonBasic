#class method:
class person:
    school_name = "Test school"

    @classmethod
    def get_school_name(cls):
        return cls.school_name;

# print(person.get_school_name())

##static method:
import datetime

class TimeUlityManager:
    @staticmethod
    def getCurrentTime():
        return datetime.datetime.now()

    @staticmethod
    def get_datetimeDifference(date):
        return datetime.datetime.now() - date
print(TimeUlityManager.getCurrentTime())
date = datetime.datetime(1992, 3, 4)
print(TimeUlityManager.get_datetimeDifference(date))
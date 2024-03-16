class person:
    school_name = "Test school"

    @classmethod
    def get_school_name(cls):
        return cls.school_name;

print(person.get_school_name())
class Person:
    def __init__(
        self,
        name,
        vital_properties,
        # courses,
        # fields_of_interest,
        # age,
        # state,
        all_properties,
        hours = None
    ):
        self.name = name
        self.vital_properties = vital_properties
        # self.courses = courses
        # self.fields_of_interest = fields_of_interest
        # self.age = age
        # self.state = state
        self.all_properties = all_properties
        self.hours = hours

    def get_name(self):
        return self.name
    
    # def get_courses(self):
    #     return self.courses

    # def get_fiels_of_interest(self):
    #     return self.fields_of_interest

    # def get_age(self):
    #     return self.age

    # def get_state(self):
    #     return self.state

    def get_property(self, index):
        return self.vital_properties[index]

    def get_vital_properties(self):
        return self.vital_properties

    def get_all_properties(self):
        return self.all_properties

    def get_hours(self):
        return self.hours
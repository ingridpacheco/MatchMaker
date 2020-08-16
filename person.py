class Person:
    def __init__(
        self,
        name,
        vital_properties,
        all_properties,
        hours = None
    ):
        self.name = name
        self.vital_properties = vital_properties
        self.all_properties = all_properties
        self.hours = hours

    def get_name(self):
        return self.name

    def get_property(self, index):
        return self.vital_properties[index]

    def get_vital_properties(self):
        return self.vital_properties

    def get_all_properties(self):
        return self.all_properties

    def get_hours(self):
        return self.hours
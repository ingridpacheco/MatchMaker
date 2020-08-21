class Person:
    def __init__(
        self,
        name,
        email,
        phone,
        vital_properties,
        all_properties,
        quantity_students,
        additional_properties = []
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.vital_properties = vital_properties
        self.all_properties = all_properties
        self.quantity_students = quantity_students
        self.additional_properties = additional_properties

    def get_information(self, type):
        information = []
        information.append(self.name),
        information.append(self.email),
        information.append(self.phone),
        information.extend(self.vital_properties)
        if (type == "student"):
            information.extend(self.additional_properties)
        return information

    def get_name(self):
        return self.name

    def get_property(self, index):
        return self.vital_properties[index]

    def get_vital_properties(self):
        return self.vital_properties

    def get_all_properties(self):
        return self.all_properties

    def get_quantity_students(self):
        return self.quantity_students

    def decrease_quantity_students(self):
        self.quantity_students -= 1

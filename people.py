class People:
    def __init__(self):
        self.list_of_person = []

    def get_person(self, name):
        for person in self.list_of_person:
            if person.get_name() == name:
                return person
        return None

    def add_person(self, person):
        self.list_of_person.append(person)

    def get_list(self):
        return self.list_of_person

    def get_names(self):
        names = []
        for person in self.list_of_person:
            names.append(person.get_name())
        return names

    
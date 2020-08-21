class People:
    def __init__(
        self,
        list_of_person = []
    ):
        self.list_of_person = list_of_person

    def get_person(self, name):
        for person in self.list_of_person:
            if person.get_name() == name:
                return person
        return None

    def add_person(self, person):
        self.list_of_person.append(person)

    
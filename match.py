class Match:
    def __init__(
        self,
        list_of_matches = {}
    ):
        self.list_of_matches = list_of_matches

    def check_match(self, student, mentor):
        match = 0
        for idx, prop_value in enumerate(mentor.get_vital_properties()):
            # print(student.get_property(idx))
            # print(mentor.get_property(idx))
            if (student.get_property(idx) == mentor.get_property(idx)):
                match += 25
        
        actual_list = self.list_of_matches.get(mentor.get_name())
        if actual_list == None:
            self.list_of_matches[mentor.get_name()] = {student.get_name(): match}
        else:
            self.list_of_matches[mentor.get_name()][student.get_name()] = match


    def get_list_of_matches(self):
        return self.list_of_matches

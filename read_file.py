import pandas as pd

class File:
    def __init__(
        self,
        file_name,
        headers,
        values,
        data_frame,
        actual_row=0,
        names_list=[],
        subjects_list=[],
        ages_list=[],
        states_list=[],
        courses_list=[]
    ):
        self.file_name = file_name
        self.headers = headers
        self.values = values
        self.data_frame = data_frame
        self.actual_row = actual_row

    def get_row(self):
        actual_row = self.values[self.actual_row]
        self.actual_row = self.actual_row + 1
        return actual_row

    def get_specific_row(self, index):
        return self.values[index]

    def get_headers(self):
        return self.headers
    
    def get_values(self):
        return self.values
    
    def get_filename(self):
        return self.values
    
    def get_name(self, index):
        return self.names_list[index]

    def get_properties(self, index):
        properties = []
        properties.append(self.subjects_list[index])
        properties.append(self.ages_list[index])
        properties.append(self.states_list[index])
        properties.append(self.courses_list[index])
        return properties

    def set_properties(self, type):
        self.names_list = self.data_frame.get('Nome completo').tolist()
        self.subjects_list = self.data_frame.get('Quais são suas disciplinas preferidas do ENEM? ').tolist()
        self.ages_list = self.data_frame.get('Idade').tolist()
        self.states_list = self.data_frame.get('Estado')
        if (type == "mentor"):
            self.courses_list = self.data_frame.get('Qual graduação você cursa/se graduou? ')
        else:
            self.courses_list = self.data_frame.get('Já sabe qual graduação pretende cursar?')
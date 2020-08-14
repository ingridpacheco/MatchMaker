import pandas as pd

class File:
    def __init__(
        self,
        file_name,
        headers,
        values,
        actual_row=0
    ):
        self.file_name = file_name
        self.headers = headers
        self.values = values
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
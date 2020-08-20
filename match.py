from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from match_interface import Match_Interface
from PyQt5.QtCore import Qt
import sys

class Match:
    def __init__(
        self,
        worksheet,
        quantity_of_headers,
        list_of_matches = {},
        actual_line = 1
    ):
        self.worksheet = worksheet
        self.quantity_of_headers = quantity_of_headers
        self.list_of_matches = list_of_matches
        self.actual_line = actual_line

    def check_match(self, student, mentor):
        match = 0
        total = 0
        reach = 60
        for idx, prop_value in enumerate(mentor.get_vital_properties()):
            mentor_props = str(prop_value).split(',')
            total += len(mentor_props)
            student_props = str(student.get_property(idx)).split(',')

            match_props = set(mentor_props).intersection(student_props)

            match += len(match_props)

        percentage = match * 100 / total
        
        if (percentage > reach):
            app = QApplication([])
            app = self.define_style(app)

            print(self.actual_line)

            match_app = Match_Interface(student, mentor, app, self.worksheet, self.quantity_of_headers, self.actual_line)

            match_app.show()
            app.exec()
            self.actual_line = match_app.get_line()

        actual_list = self.list_of_matches.get(mentor.get_name())
        if actual_list == None:
            self.list_of_matches[mentor.get_name()] = {student.get_name(): percentage}
        else:
            self.list_of_matches[mentor.get_name()][student.get_name()] = percentage

    def define_style(self, app):
        app.setStyle("Fusion")

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)

        app.setPalette(palette)
        app.setApplicationName("Match found!")
        return app

    def get_list_of_matches(self):
        return self.list_of_matches
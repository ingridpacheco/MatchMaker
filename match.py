from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from match_interface import Match_Interface
from PyQt5.QtCore import Qt
import sys

class Match:
    def __init__(
        self,
        list_of_matches = {}
    ):
        self.list_of_matches = list_of_matches

    def check_match(self, student, mentor):
        match = 0
        total = 0
        for idx, prop_value in enumerate(mentor.get_vital_properties()):
            mentor_props = str(prop_value).split(',')
            total += len(mentor_props)
            student_props = str(student.get_property(idx)).split(',')

            match_props = set(mentor_props).intersection(student_props)

            match += len(match_props)

        percentage = match * 100 / total
        
        actual_list = self.list_of_matches.get(mentor.get_name())
        if actual_list == None:
            self.list_of_matches[mentor.get_name()] = {student.get_name(): percentage}
        else:
            self.list_of_matches[mentor.get_name()][student.get_name()] = percentage

        if (percentage > 60):
            app = QApplication([])
            app = self.define_style(app)
            
            match_app = Match_Interface(student, mentor, app)
            match_app.show()
            app.exec()

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
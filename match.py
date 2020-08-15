from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt

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

        self.create_interface(student, mentor)

    def create_interface(self, student, mentor):
        self.app = QApplication([])
        self.app.setStyle("Fusion")

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)

        self.app.setPalette(palette)

        self.app.setApplicationName("Match found!")

        topLeftGroupBox = QGroupBox("Group 1")

        layout = QVBoxLayout()

        student_info = QLabel(student.get_name())
        student_info.show()

        mentor_info = QLabel(mentor.get_name())
        mentor_info.show()

        yes_button = QPushButton('Sim')
        yes_button.clicked.connect(self.on_button_clicked)
        no_button = QPushButton('Não')
        no_button.clicked.connect(self.on_button_clicked)

        layout.addWidget(student_info)
        layout.addWidget(mentor_info)
        layout.addWidget(yes_button)
        layout.addWidget(no_button)

        topLeftGroupBox.setLayout(layout)

        topLeftGroupBox.show()
        self.app.exec_()

    def on_button_clicked(self):
        self.app.quit()
        # alert = QMessageBox()

        # alert.setText('sim')
        # alert.exec_()

    def get_list_of_matches(self):
        return self.list_of_matches
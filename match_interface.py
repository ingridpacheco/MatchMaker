from PyQt5.QtWidgets import *

class Match_Interface(QDialog):
    def __init__(
        self,
        student,
        mentor,
        app,
        worksheet,
        headers,
        line,
        accepted = False
    ):

        self.student = student
        self.mentor = mentor
        self.app = app
        self.worksheet = worksheet
        self.headers = headers
        self.line = line
        self.accepted = accepted

        super(Match_Interface, self).__init__()

        self.create_student()
        self.create_mentor()
        self.create_buttons()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.studentGroupBox, 0, 0)
        mainLayout.addWidget(self.mentorGroupBox, 0, 1)
        mainLayout.addLayout(self.bottomLayout, 1, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    def create_buttons(self):
        self.bottomLayout = QHBoxLayout()

        yes_button = QPushButton('Sim')
        yes_button.clicked.connect(self.accept_match)
        no_button = QPushButton('Não')
        no_button.clicked.connect(self.reject_match)

        self.bottomLayout.addWidget(yes_button)
        self.bottomLayout.addWidget(no_button)
        self.bottomLayout.addStretch(1)

    def create_student(self):
        self.studentGroupBox = QGroupBox("Student")

        student_info = QLabel(self.student.get_name())
        student_info.show()

        layout = QVBoxLayout()
        layout.addWidget(student_info)
        layout = self.render_properties(self.student.get_vital_properties(), layout)
        layout.addStretch(1)

        self.studentGroupBox.setLayout(layout)

    def create_mentor(self):
        self.mentorGroupBox = QGroupBox("Mentor")

        mentor_info = QLabel(self.mentor.get_name())
        mentor_info.show()

        layout = QVBoxLayout()
        layout.addWidget(mentor_info)
        layout = self.render_properties(self.mentor.get_vital_properties(), layout)
        layout.addStretch(1)

        self.mentorGroupBox.setLayout(layout)

    def accept_match(self):
        output = self.mentor.get_information("mentor") + self.student.get_information("student")
        
        for i in range(self.headers):
            self.worksheet.write(self.line, i, str(output[i]))

        self.line += 1
        self.accepted = True
        self.app.quit()

    def reject_match(self):
        self.app.quit()

    def get_acceptation(self):
        return self.accepted

    def render_properties(self, properties, layout):
        for property_info in properties:
            property_label = QLabel(str(property_info))
            property_label.show()

            layout.addWidget(property_label)
        
        return layout

    def get_line(self):
        return self.line


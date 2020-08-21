# -*- coding: utf-8 -*-

import pandas as pd
import xlsxwriter
from read_file import File
from person import Person
from match import Match
from people import People

def main(student_file, volunteer_file, output_file):

    workbook = xlsxwriter.Workbook('/Users/Ingrid.Pacheco/Desktop/match-output.xlsx')
    worksheet = workbook.add_worksheet()
    headers = ['nome MENTOR', 'email MENTOR', 'numero MENTOR', 'graduacao MENTOR', 'disciplinas MENTOR', 'idade MENTOR', 'estado MENTOR', 'nome ALUNO', 'email ALUNO', 'numero ALUNO', 'graduacao ALUNO', 'disciplinas ALUNO', 'idade ALUNO', 'estado ALUNO', 'dificuldades', 'interesse']
    worksheet = add_headers(worksheet, headers)
    matches = Match(worksheet, len(headers))
    students = People()
    mentors = People()
    with pd.ExcelFile(student_file) as firstxls:
        df1 = pd.read_excel(firstxls, 0)

        f1 = File(student_file, df1.columns, df1.values.tolist(), df1)
        f1.set_properties('student')

        with pd.ExcelFile(volunteer_file) as secondxls:
                df2 = pd.read_excel(secondxls, 0)

                f2 = File(volunteer_file, df2.columns, df2.values.tolist(), df2)
                f2.set_properties('mentor')

                hours = df2.get('Quantas horas por semana você terá para dedicar para a mentoria (não esqueça de levar em consideração o tempo que você já dedica a outras atividades, e eventualmente outros projetos do ExplicaEnem que você é parte).  Dessa maneira, de acordo com sua disponibilidade, poderemos te conectar com a quantidade de mentorados.').tolist()
                for idx_mentor, val_mentor in enumerate(f2.get_values()):

                    vital_properties = f2.get_properties(idx_mentor, 'mentor')
                    mentor = Person(f2.get_name(idx_mentor), f2.get_email(idx_mentor), f2.get_phone(idx_mentor), vital_properties, val_mentor, int(hours[idx_mentor].split('(')[1].split(' ')[0]))
                    mentors.add_person(mentor)

                    for idx_student, val_student in enumerate(f1.get_values()):

                        student_vital_properties = f1.get_properties(idx_student, 'student')
                        student = Person(f1.get_name(idx_student), f1.get_email(idx_student), f1.get_phone(idx_student), student_vital_properties, val_student, 0, f1.get_additional_properties(idx_student))
                        students.add_person(student)

                        matches.get_match(student, mentor)
    
    find_matches(matches, students, mentors)
    workbook.close()

def find_matches(matches, students, mentors):
    mentor_list = []

    for student_name in matches.get_list_of_matches().keys():
        student = students.get_person(student_name)
        for mentor_name in sorted(matches.get_list_of_matches()[student_name], key=matches.get_list_of_matches()[student_name].get, reverse=True):
            mentor = mentors.get_person(mentor_name)
            if (mentor_name not in mentor_list) and (int(mentor.get_quantity_students()) > 0):
                accepted = matches.check_match(student, mentor)
                if (accepted):
                    print('Match: {} & {}'.format(mentor_name, student_name))
                    mentor.decrease_quantity_students()
                    mentor_list.append(mentor_name)
                    break;

def add_headers(worksheet, headers):
    for i in range(len(headers)):
        worksheet.write(0, i, headers[i])
    return worksheet

if __name__ == "__main__":
    student_file = str(input("Students file: "))
    mentor_file = str(input("Mentors file: "))
    output_file = str(input("Output file: "))
    main(student_file, mentor_file, output_file)
    # main("/Users/Ingrid.Pacheco/Downloads/Formulário-Alunos(respostas).xlsx", "/Users/Ingrid.Pacheco/Downloads/Mentores-Pareamento.xlsx", "/Users/Ingrid.Pacheco/Downloads/alunos-selecionados-mentoria-turma1.xlsx")
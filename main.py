# -*- coding: utf-8 -*-

import pandas as pd
from read_file import File
from person import Person
from match import Match

def main(student_file, volunteer_file, output_file):

    matches = Match()
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

                    vital_properties = f2.get_properties(idx_mentor)
                    mentor = Person(f2.get_name(idx_mentor), vital_properties, val_mentor, hours[idx_mentor])

                    for idx_student, val_student in enumerate(f1.get_values()):

                        student_vital_properties = f1.get_properties(idx_student)
                        student = Person(f1.get_name(idx_student), student_vital_properties, val_student)

                        matches.check_match(student, mentor)

    print(matches.get_list_of_matches())

#/Users/Ingrid.Pacheco/Downloads/alunos-selecionados-mentoria-turma1.xlsx
if __name__ == "__main__":
    # first_file = str(input("Students file: "))
    # second_file = str(input("Volunteers file: "))
    # output_file = str(input("Output file: "))
    # main(first_file, second_file, output_file)
    main("/Users/Ingrid.Pacheco/Downloads/Formulário-Alunos(respostas).xlsx", "/Users/Ingrid.Pacheco/Downloads/Mentores-Pareamento.xlsx", "/Users/Ingrid.Pacheco/Downloads/alunos-selecionados-mentoria-turma1.xlsx")

#ALUNOS =>  Carimbo de data/hora, Nome completo, E-mail utilizado no formulário de cadastro, Número de telefone com DDD (WhatsApp), Já sabe qual graduação pretende cursar?, Quais são suas disciplinas preferidas do ENEM?, Na sua visão, quais são as maiores dificuldades que você enfrenta hoje ao se preparar para o ENEM?,Porque você se interessou pela mentoria?, Idade, Estado
#VOLUNTARIOS => Carimbo de data/hora, Nome completo, E-mail utilizado no formulário de cadastro, Número de telefone com DDD (WhatsApp), Quantas horas por semana você terá para dedicar para a mentoria (não esqueça de levar em consideração o tempo que você já dedica a outras atividades, e eventualmente outros projetos do ExplicaEnem que você é parte).  Dessa maneira, de acordo com sua disponibilidade, poderemos te conectar com a quantidade de mentorados., Li, estou ciente e concordo com o Termo de Compromisso da Mentoria ExplicaEnem. Você pode conferí-lo aqui: https://docs.google.com/document/d/19zEpUVSIRajL3aOn-hroMNiTWzpbFLH9DETz_z6OeTM/edit?usp=sharing, Na sua visão, qual a sua responsabilidade como mentor?, Por que você deseja ser mentor?, Qual graduação você cursa/se graduou?, Quais são suas disciplinas preferidas do ENEM?, Idade, Estado
# para cada mentor na planilha B, verificar nos alunos:
# -> Já sabe qual graduação pretende cursar? (aluno) | Qual graduação você cursa/se graduou? (mentor)
# -> Idade (aluno) | Idade (mentor)
# -> Estado (aluno) | Estado (mentor)
# -> Quais são suas disciplinas preferidas do ENEM? (aluno) | Quais são suas disciplinas preferidas do ENEM? (mentor)
# Para cada mentor, grava a porcentagem de match com cada aluno => {'mentorA': {'Aluno A': 50, 'Aluno B': 70}}... Se match > 80 % já pergunta, se não, guarda no dicionário
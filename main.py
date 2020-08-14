import pandas as pd
from read_file import File

def main(student_file, volunteer_file, output_file):
    with pd.ExcelFile(student_file) as firstxls:
        df1 = pd.read_excel(firstxls, 0)
        f1 = File(student_file, df1.columns, df1.values.tolist())
        with pd.ExcelFile(volunteer_file) as secondxls:
                df2 = pd.read_excel(secondxls, 0)
                f2 = File(volunteer_file, df2.columns, df2.values.tolist())
                # print(f1.get_specific_row(3))
                # print(f1.get_row())
                for row in f2.get_values():
#/Users/Ingrid.Pacheco/Downloads/alunos-selecionados-mentoria-turma1.xlsx

if __name__ == "__main__":
    # first_file = str(input("Students file: "))
    # second_file = str(input("Volunteers file: "))
    # output_file = str(input("Output file: "))
    # main(first_file, second_file, output_file)
    main("/Users/Ingrid.Pacheco/Downloads/alunos-selecionados-mentoria-turma1.xlsx", "/Users/Ingrid.Pacheco/Downloads/alunos-selecionados-mentoria-turma1.xlsx", "/Users/Ingrid.Pacheco/Downloads/alunos-selecionados-mentoria-turma1.xlsx")

# ARQUIVO A => pessoas em cada coluna com atributos
# ARQUIVO B => pessoas em cada coluna com atributos
# para cada pessoa A eu vou passar em cada pessoa B verificando os atributos x e y
# se der match, manda para uma matriz
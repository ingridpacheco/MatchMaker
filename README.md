![Image of Match Maker](img/matchmaker.png)

Match Maker is a program that finds matches between two instances in different spreadsheets and outputs them in another file. In this first version, initially designed to work for ExplicaENEM, it has previously selected headers, not allowing flexiblity on their choices.

## Dependencies
- pandas
- xlrd
- PyQt5 (5.9.2)
- xlsxwriter

## How to use

- Clone the repository (https://github.com/ingridpacheco/MatchMaker)
- Be sure to have Python2 or Python3 (with pip) in your environment
- Run: `make setup`
- Run: `make run`
- Fill the program inputs with the correct files with their full paths
- Accept the matches you like and reject the matches you dislike
- After the program finishes, check the matches in the output file

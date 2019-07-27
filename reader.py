from os import path
from variable import Variable
from clause import Clause
from cnf import Cnf


class Reader:
    def __init__(self, input_folder_name='inputs'):
        self.input_folder_name = input_folder_name
        self.this_file_path = path.dirname(path.abspath(__file__))
        print(self.this_file_path)

    def read(self, file_name):
        file_path = path.join(path.join(self.this_file_path, self.input_folder_name), file_name)
        print(file_path)
        file = open(file_path, 'r').read()
        rows = file.split('\n')

        clause_list = list()
        for row in rows:
            if row[0] != 'c' and row[0] != 'p':
                var_list = list()
                for var in row.split(' '):
                    var_list.append(Variable(var))
                clause_list.append(Clause(var_list))

        cnf = Cnf(clause_list)

        return cnf

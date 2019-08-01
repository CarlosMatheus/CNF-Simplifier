from cnf import Cnf
from clause import Clause
from variable import Variable
from random import random as rd
from writer import Writer


class InputGenerator:
    def __init__(self, num_of_var=20, num_of_clause=50, num_of_var_per_clause=4, variation=0.5):
        self.num_of_var = num_of_var
        self.num_of_clause = num_of_clause
        self.variation = variation
        self.num_of_var_per_clause = num_of_var_per_clause

    def get_variation(self, size):
        variation = self.variation * size
        variation = round(rd() * variation)
        if rd() > 0.5:
            variation *= -1
        return int(variation)

    def generate_and_write_inputs(self, folder_name, num_of_inputs):
        for i in range(num_of_inputs + 1):
            cnf = self.generate()
            writer = Writer(folder_name)
            file_name = ('output%0{}d.txt'.format(len(str(num_of_inputs)))) % i
            writer.write(file_name, cnf)

    def generate(self):
        num_of_var = self.num_of_var + self.get_variation(self.num_of_var)
        num_of_clause = self.num_of_clause + self.get_variation(self.num_of_clause)

        clause_list = list()
        for i in range(num_of_clause):
            num_of_var_per_clause = self.num_of_var_per_clause + self.get_variation(self.num_of_var_per_clause)
            var_list = list()
            for j in range(num_of_var_per_clause):
                signal = 1
                if rd() > 0.5:
                    signal = -1
                var_str = str(int(signal * round(num_of_var * rd() + 1)))
                var = Variable(var_str)
                var_list.append(var)
            clause = Clause(var_list)
            clause_list.append(clause)

        cnf = Cnf(clause_list)

        return cnf

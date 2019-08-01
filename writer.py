from os import path
import os
from cnf import Cnf


class Writer:
    def __init__(self, output_folder_name='outputs'):
        self.output_folder_name = output_folder_name
        self.this_file_path = path.dirname(path.abspath(__file__))
        if not path.exists(path.join(self.this_file_path, self.output_folder_name)):
            os.mkdir(path.join(self.this_file_path, self.output_folder_name))

    def write(self, file_name, cnf: Cnf):

        file_path = path.join(path.join(self.this_file_path, self.output_folder_name), file_name)

        print('writing: ' + str(file_path))

        num_clause = cnf.get_number_of_clauses()
        num_literals = cnf.get_number_of_literals()

        title = 'c\nc start with comments\nc\np cnf %d %d\n' % (num_literals, num_clause)

        open(file_path, 'w').write(title + cnf.get_cnf_string(with_zero=True))

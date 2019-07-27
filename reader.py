from os import path


class Reader:
    def __init__(self, input_folder_name='inputs'):
        self.input_folder_name = input_folder_name
        self.this_file_path = path.dirname(path.abspath(__file__))
        print(self.this_file_path)

    def read(self, file_name):
        file_path = path.join(path.join(self.this_file_path, self.input_folder_name), file_name)
        print(file_path)
        file = open(file_path, 'r').read()

        return file




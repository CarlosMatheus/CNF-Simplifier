import reader
from writer import Writer
from simplifier import Simplifier
from input_generator import InputGenerator

def execute(i):
    rd = reader.Reader()
    input_name = 'input0' + str(i) + '.txt'
    output_name = 'output0' + str(i) + '.txt'

    cnf = rd.read(input_name)
    print(len(cnf.clause_list))
    print(cnf.get_cnf_string())

    simplifier = Simplifier()

    complete_simplified_cnf = simplifier.complete(cnf)
    print()
    print(len(complete_simplified_cnf.clause_list))
    print(complete_simplified_cnf.get_cnf_string())

    writer = Writer()
    writer.write(output_name, complete_simplified_cnf)

if __name__ == '__main__':
    # execute(0)
    # execute(1)
    # execute(3)
    # execute(4)
    InputGenerator().generate_and_write_inputs('test_folder', 50)

import reader
from simplifier import Simplifier

def execute(i):
    rd = reader.Reader()
    cnf = rd.read('input0' + str(i) + '.txt')
    print(len(cnf.clause_list))
    print(cnf.get_cnf_string())

    simplifier = Simplifier()

    complete_simplified_cnf = simplifier.complete(cnf)
    print()
    print(len(complete_simplified_cnf.clause_list))
    print(complete_simplified_cnf.get_cnf_string())

if __name__ == '__main__':
    execute(3)
    execute(4)

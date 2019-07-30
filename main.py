import reader
from simplifier import Simplifier

if __name__ == '__main__':
    rd = reader.Reader()
    cnf = rd.read('input00.txt')
    print(cnf.get_cnf_string())

    simplifier = Simplifier()

    complete_simplified_cnf = simplifier.complete(cnf)
    print()
    print(cnf.get_cnf_string())

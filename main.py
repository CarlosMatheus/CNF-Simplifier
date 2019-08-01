import reader
from writer import Writer
from simplifier import Simplifier
from input_generator import InputGenerator


def execution(function, rd, writer, input_name, output_name, function_name, data_hash):
    cnf = rd.read(input_name)
    initial_num_of_clause = cnf.get_number_of_clauses()
    complete_simplified_cnf = function(cnf)
    final_num_of_clause = complete_simplified_cnf.get_number_of_clauses()
    writer.write(output_name, complete_simplified_cnf)

    print(function_name)
    if function_name in data_hash:
        data_hash[function_name].append(1 - final_num_of_clause/initial_num_of_clause)
    else:
        data_hash[function_name] = [1 - final_num_of_clause / initial_num_of_clause]


def execute(input_folder_name, output_folder_name, file_num, data_hash):
    input_name = ('input%0{}d.txt'.format(len(str(number_of_files)))) % file_num
    output_name = ('output%0{}d.txt'.format(len(str(number_of_files)))) % file_num

    rd = reader.Reader(input_folder_name=input_folder_name)
    writer = Writer(output_folder_name=output_folder_name)

    simplifier = Simplifier()

    execution_lt = [
        (simplifier.tautoly, "tautoly"),
        (simplifier.blocked_clause, "blocked_clause"),
        (simplifier.subsumption_elimination, "subsumption_elimination"),
        (simplifier.hidden_tautoly, "hidden_tautoly"),
        (simplifier.hidden_blocked_clause, "hidden_blocked_clause"),
        (simplifier.hidden_subsumption_elimination, "hidden_subsumption_elimination"),
        (simplifier.explicits, "explicits"),
        (simplifier.hiddens, "hiddens"),
        (simplifier.complete, "Complete"),
    ]

    # Just Tautology:

    # Just Blocked Clause:

    # Just Subsumed Clause:

    # Hidden Tautology:

    # Hidden Blocked Clause:

    # Hidden Subsumed:

    # simples

    # Hidden

    for function, function_name in execution_lt:
        execution(function, rd, writer, input_name, output_name, function_name, data_hash)


if __name__ == '__main__':
    number_of_files = 2
    base_var_num = 20
    var_num = base_var_num
    clause_num = base_var_num * 3

    for i in range(1, 2):

        input_folder_name = 'inputs' + str(i)
        output_folder_name = 'outputs' + str(i)

        InputGenerator(
            num_of_var=var_num,
            num_of_clause=clause_num
        ).generate_and_write_inputs(input_folder_name, number_of_files)

        data_hash = {}
        for file_num in range(number_of_files):
            execute(input_folder_name, output_folder_name, file_num, data_hash)

        print(str(i) + ': ')
        print('var_num ' + str(var_num) + ' +- ' + str(var_num/2))
        print('clause_num ' + str(clause_num) + ' +- ' + str(clause_num/2))

        for function_name in data_hash.keys():
            lt = data_hash[function_name]
            print('in function ' + function_name)
            print('for ' + str(len(lt)) + ' cases')
            print('mean reduction was ' + str(sum(lt)/len(lt)))
            print('max reduction was ' + str(max(lt)))
            print('min reduction was ' + str(min(lt)))
            print(lt)

        print()

        var_num *= 2
        clause_num *= 2

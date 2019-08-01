import reader
from writer import Writer
from simplifier import Simplifier
from input_generator import InputGenerator
import time


def execution(function, rd, writer, input_name, output_name, function_name, data_hash):
    cnf = rd.read(input_name)
    initial_num_of_clause = cnf.get_number_of_clauses()
    initial_time = time.time()
    complete_simplified_cnf = function(cnf)
    final_time = time.time()
    final_num_of_clause = complete_simplified_cnf.get_number_of_clauses()
    writer.write(output_name, complete_simplified_cnf)

    print(function_name)
    if function_name in data_hash:
        data_hash[function_name].append( (1 - final_num_of_clause/initial_num_of_clause, final_time - initial_time) )
    else:
        data_hash[function_name] = [ (1 - final_num_of_clause / initial_num_of_clause, final_time - initial_time ) ]


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
        (simplifier.asymmetric_tautoly, "asymmetric_tautoly"),
        (simplifier.asymmetric_blocked_clause, "asymmetric_blocked_clause"),
        (simplifier.asymmetric_subsumption_elimination, "asymmetric_subsumption_elimination"),
        (simplifier.explicits, "explicits"),
        (simplifier.hiddens, "hiddens"),
        (simplifier.asymmetrics, "asymmetrics"),
        (simplifier.complete, "Complete"),
    ]

    for function, function_name in execution_lt:
        execution(function, rd, writer, input_name, output_name, function_name, data_hash)


if __name__ == '__main__':

    file = open('results.txt', 'w')

    number_of_files = 1
    base_var_num = 20
    var_num = base_var_num
    clause_num = base_var_num * 3

    loop_exp_factor = 1.3
    num_of_loops = 2

    for i in range(1, num_of_loops + 1):

        input_folder_name = 'inputs' + str(i)
        output_folder_name = 'outputs' + str(i)

        InputGenerator(
            num_of_var=var_num,
            num_of_clause=clause_num
        ).generate_and_write_inputs(input_folder_name, number_of_files)

        data_hash = {}
        for file_num in range(number_of_files):
            execute(input_folder_name, output_folder_name, file_num, data_hash)

        lt = list()

        lt.append(str(i) + ': ')
        lt.append('var_num ' + str(var_num) + ' +- ' + str(var_num/2))
        lt.append('clause_num ' + str(clause_num) + ' +- ' + str(clause_num/2))
        lt.append('for ' + str(number_of_files) + ' number_of_files\n')

        for function_name in data_hash.keys():
            data_lt = []
            time_lt = []
            for elm in data_hash[function_name]:
                data_lt.append(elm[0])
                time_lt.append(elm[1])

            lt.append('in function ' + function_name)
            lt.append('average time per cnf was ' + str(sum(time_lt)/len(time_lt)))
            lt.append('average reduction was ' + str(sum(data_lt)/len(data_lt)))
            lt.append('max reduction was ' + str(max(data_lt)))
            lt.append('min reduction was ' + str(min(data_lt)))
            lt.append(str(data_lt))
            lt.append('')

        lt.append('\n=================================\n')

        for elm in lt:
            print(elm)

        file.write('\n'.join(lt))

        var_num = int(var_num * loop_exp_factor)
        clause_num = int(clause_num * loop_exp_factor)

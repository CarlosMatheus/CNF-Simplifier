import utils


class Clause:
    def __init__(self, variable_list):
        self.variable_list = variable_list
        self.size = len(self.variable_list)
        self.id = utils.create_id()

        self.literals_set = set()
        for var in variable_list:
            self.literals_set.add(var.variable_value)

    def copy_with_new_id(self):
        """
        Copy this clause to a new one with new id and new literals
        :complexity: O(n) where n in the number of literals inside the clause
        :return: Clause
        """
        new_variable_list = [lit.copy() for lit in self.variable_list] # todo: make copy function
        new_clause = Clause(new_variable_list)
        return new_clause

    def is_literal_value_present(self, literal_value: int):
        return literal_value in self.literals_set

    def get_literals(self):
        return self.variable_list

    def get_literals_sub_sets(self):
        """
        Get all literals sub sets excluding the empty set
        this is done in O(n2^n), where n is the number of literals in the clause
        :return: all sub sets
        """
        def rec(i, curr, literals, ans):
            if i == len(literals) and curr:
                ans.append(curr)
            else:
                copied = curr.copy()
                copied.append(literals[i])
                rec(i+1, curr, literals, ans)
                rec(i+1, copied, literals, ans)

        variables = self.variable_list
        sub_sets = list()
        rec(0, [], variables, sub_sets)

        return sub_sets

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

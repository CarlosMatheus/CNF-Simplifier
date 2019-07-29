import utils
from variable import Variable


class Clause:
    def __init__(self, variable_list):
        self.variable_list = variable_list
        self.size = len(self.variable_list)
        self.id = utils.create_id()

        self.literals_set = set()
        for var in variable_list:
            self.literals_set.add(var.variable_value)

    def add_literal(self, lit):
        """
        Add a new literal to the clause
        :complexity: O(1)
        :param lit: the literal object of the Variable class
        :return: None
        """
        self.variable_list.append(lit)
        self.size = len(self.variable_list)
        self.literals_set.add(lit.variable_value)

    def copy_with_new_id(self):
        """
        Copy this clause to a new one with new id and new literals
        :complexity: O(n) where n in the number of literals inside the clause
        :return: Clause
        """
        new_variable_list = [lit.copy() for lit in self.variable_list]
        new_clause = Clause(new_variable_list)
        return new_clause

    def is_sub_clause_of(self, other_clause):
        """
        checks wheater a clause is a subclause of the other one
        :complexity: O(n) where n is the number of literal present on this class
        :param other_clause: the other clause
        :return: boolean
        """
        for lit in self.get_literals():
            if not other_clause.has_literal(lit):
                return False
        return True

    def has_literal(self, lit: Variable):
        """
        Checkes whether a literal objesct is present on a clause
        :complexity: O(1)
        :param lit: literal obejesct of class Variable
        :return: boolean
        """
        return self.is_literal_value_present(lit.variable_value)

    def is_literal_value_present(self, literal_value: int):
        """
        checkes whether a literal value int is present on literal set
        :complexity: O(1) -> set check uses a hashtable, worse case could be O(n)
        :param literal_value: literal value to check
        :return: boolean
        """
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

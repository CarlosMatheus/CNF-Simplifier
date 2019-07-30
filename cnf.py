from clause import Clause


class Cnf:
    def __init__(self, clause_list: list):
        self.clause_list = clause_list

    def get_clauses(self):
        """
        Return clause list
        :complexity: O(1)
        :return: clause list
        """
        return self.clause_list

    def add_clause(self, clause):
        """
        Add a new clause to the CNF
        :complexity: O(1)
        :param clause: clause to add
        :return: add a new clause
        """
        if not isinstance(clause, Clause):
            raise Exception("Expected type Clause, and got %s" % type(clause))

        self.clause_list.append(clause)

    def tautology_elimination(self):
        """
        Simplify CNF by removing all clauses that are tautology
        :complexity: O(c*l)
        :return: a new CNF without tautological clauses
        """

        new_cnf = Cnf([])
        for clause in self.clause_list:
            if not clause.is_tautology():
                copied_clause = clause.copy_with_new_id()
                new_cnf.add_clause(copied_clause)

        return new_cnf

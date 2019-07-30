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

    def hidden_tautology_elimination(self):
        """
        Simplify CNF by removing all clauses that are hidden tautology

        :complexity: O( (c*l)^2 )
        :return: a new CNF without hidden tautological clauses
        """
        new_cnf = Cnf([])
        for clause in self.clause_list:
            hla_clause = clause.hla(self)
            if not hla_clause.is_tautology():
                new_cnf.add_clause(clause)

        return new_cnf

    def asymmetric_tautology_elimination(self):
        """
        Simplify CNF by removing all clauses that are asymmetric tautology

        :complexity: O( c^2 * l^2 * 2^l )
        :return: a new CNF without asymmetric tautological clauses
        """
        new_cnf = Cnf([])
        for clause in self.clause_list:
            ala_clause = clause.ala(self)
            if not ala_clause.is_tautology():
                new_cnf.add_clause(clause)

        return new_cnf

    def blocked_clause_elimination(self):
        """
        Simplify CNF by removing all clauses that are blocked
        :complexity: O( (c*l)^2 )
        :return: a new CNF without blocked clauses
        """

        new_cnf = Cnf([])
        for clause in self.clause_list:
            if not clause.is_blocked():
                copied_clause = clause.copy_with_new_id()
                new_cnf.add_clause(copied_clause)

        return new_cnf

    def hidden_blocked_clause_elimination(self):
        """
        Simplify CNF by removing all clauses that are hidden blocked

        :complexity: O( (c*l)^2 )
        :return: a new CNF without hidden blocked clauses
        """
        new_cnf = Cnf([])
        for clause in self.clause_list:
            hla_clause = clause.hla(self)
            if not hla_clause.is_blocked():
                new_cnf.add_clause(clause)

        return new_cnf

    def asymmetric_blocked_clause_elimination(self):
        """
        Simplify CNF by removing all clauses that are asymmetric blocked

        :complexity: O( c^2 * l^2 * 2^l )
        :return: a new CNF without asymmetric blocked clauses
        """
        new_cnf = Cnf([])
        for clause in self.clause_list:
            ala_clause = clause.ala(self)
            if not ala_clause.is_blocked():
                new_cnf.add_clause(clause)

        return new_cnf

    def subsumption_elimination(self):
        """
        Simplify CNF by removing all clauses that are subsumed

        :complexity: O(  )

        :return: a new CNF without subsumed clauses
        """

        new_cnf = Cnf([])
        for clause in self.clause_list:
            if not clause.is_subsumed():
                copied_clause = clause.copy_with_new_id()
                new_cnf.add_clause(copied_clause)

        return new_cnf

    def hidden_subsumption_elimination(self):
        """
        Simplify CNF by removing all clauses that are hidden subsumed
        :complexity: O( (l*c)^2 )
        :return: a new CNF without hidden subsumed clauses
        """
        new_cnf = Cnf([])
        for clause in self.clause_list:
            hla_clause = clause.hla(self)
            if not hla_clause.is_subsumed():
                new_cnf.add_clause(clause)

        return new_cnf

    def asymmetric_subsumption_elimination(self):
        """
        Simplify CNF by removing all clauses that are asymmetric subsumed

        :complexity: O( c^2 * l^2 * 2^l )
        :return: a new CNF without asymmetric subsumed clauses
        """
        new_cnf = Cnf([])
        for clause in self.clause_list:
            ala_clause = clause.ala(self)
            if not ala_clause.is_subsumed():
                new_cnf.add_clause(clause)

        return new_cnf

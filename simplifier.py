from clause import Clause


class Simplifier:
    def __init__(self):
        pass

    def hla(self, f, c):
        """
        # todo: test
        Hidden Literal Addition HLA(F,C)
        :complexity: todo
        :param f: CNF
        :param c: Clause
        :return: HLA(F,C)
        """
        c_hla = c.copy_with_new_id()

        for lit in c.get_literals():
            for clause in f.get_clauses():
                if clause != c:
                    if clause.size == 2:
                        lit_clause = Clause([lit])
                        if lit_clause.is_sub_clause_of(clause):

                            dif = clause.get_diff(lit_clause)
                            lit = dif[0].copy()

                            c_hla.add_literal(lit)

        return c_hla

    def ala(self, f, c):
        """
        # todo: test
        Asymmetric Literal Addition ALA(F,C)
        :complexity: todo
        :param f:
        :param c:
        :return:
        """
        c_ala = c.copy_with_new_id()

        sub_sets = c.get_literals_sub_sets()

        for literal_sub_set in sub_sets:
            for clause in f.get_clauses():
                if clause != c:
                    sub_clause = Clause(literal_sub_set)
                    if clause.size == sub_clause.size + 1:
                        if sub_clause.is_sub_clause_of(clause):
                            dif = clause.get_diff(sub_clause)
                            lit = dif[0].copy()

                            c_ala.add_literal(lit)

        return c_ala

    def is_subsumed_clause(self, clause, cnf):
        """
        todo: Verify if it is necessary to verify if they are different
        todo: this might belong to the clause class
        :complexity: todo
        :param clause: the evaluated clause
        :param cnf: The cnf that the clause belong
        :return: boolean
        """
        for other_clause in cnf.get_clauses():
            if other_clause.is_different(clause):
                # todo: verify if that is the correct order:
                if other_clause.is_sub_clause_of(clause):
                    return True
        return False


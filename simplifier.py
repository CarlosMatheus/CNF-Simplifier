class Simplifier:
    def __init__(self):
        pass

    def hla(self, f, c):
        """
        # todo: test
        # todo: get complexity order
        Hidden Literal Addition HLA(F,C)
        :param f: CNF
        :param c: Clause
        :return: HLA(F,C)
        """
        c_hla = c.copy_with_new_id() # create

        for lit in c.get_literals():
            for clause in f.get_clauses():
                if clause != c:
                    if clause.size == 2:
                        lit_clause = Clause([lit])
                        if lit_clause.is_sub_clause_of(clause): # create
                            dif = clause.get_dif(sub_clause) # create
                            lit = dif[0].copy_with_new_id() # create

                            c_hla.add_literal(lit)

        return c_hla

    def ala(self, f, c):
        """
        # todo: test
        # todo: get complexity order
        Asymmetric Literal Addition ALA(F,C)
        :param f:
        :param c:
        :return:
        """
        c_ala = c.copy_with_new_id() # create

        sub_sets = c.get_literals_sub_sets()

        for literal_sub_set in sub_sets:
            for clause in f.get_clauses():
                if clause != c:
                    sub_clause = Clause(literal_sub_set)
                    if clause.size == sub_clause.size + 1:
                        if sub_clause.is_sub_clause_of(clause): # create
                            dif = clause.get_dif(sub_clause) # create
                            lit = dif[0].copy_with_new_id() # create

                            c_ala.add_literal(lit)

        return c_ala

from clause import Clause


class Simplifier:
    def __init__(self):
        pass

    def complete(self, cnf):

        # cnf = cnf.tautology_elimination()
        cnf = cnf.blocked_clause_elimination()
        # cnf = cnf.subsumption_elimination()

        # cnf = cnf.hidden_tautology_elimination()
        # cnf = cnf.asymmetric_tautology_elimination()

        cnf = cnf.hidden_blocked_clause_elimination()
        cnf = cnf.asymmetric_blocked_clause_elimination()
        #
        # cnf = cnf.hidden_subsumption_elimination()
        # cnf = cnf.asymmetric_subsumption_elimination()

        return cnf

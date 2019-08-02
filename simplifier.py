from clause import Clause


class Simplifier:
    def __init__(self):
        pass

    def tautoly(self, cnf):
        cnf = cnf.tautology_elimination()
        return cnf

    def blocked_clause(self, cnf):
        cnf = cnf.blocked_clause_elimination()
        return cnf

    def subsumption_elimination(self, cnf):
        cnf = cnf.subsumption_elimination()
        return cnf

    def hidden_tautoly(self, cnf):
        cnf = cnf.hidden_tautology_elimination()
        return cnf

    def hidden_blocked_clause(self, cnf):
        cnf = cnf.hidden_blocked_clause_elimination()
        return cnf

    def hidden_subsumption_elimination(self, cnf):
        cnf = cnf.hidden_subsumption_elimination()
        return cnf

    def asymmetric_tautoly(self, cnf):
        cnf = cnf.asymmetric_tautology_elimination()
        return cnf

    def asymmetric_blocked_clause(self, cnf):
        cnf = cnf.asymmetric_blocked_clause_elimination()
        return cnf

    def asymmetric_subsumption_elimination(self, cnf):
        cnf = cnf.asymmetric_subsumption_elimination()
        return cnf

    def explicits(self, cnf):
        cnf = cnf.subsumption_elimination()
        cnf = cnf.blocked_clause_elimination()
        cnf = cnf.tautology_elimination()
        return cnf

    def hiddens(self, cnf):
        cnf = cnf.hidden_subsumption_elimination()
        cnf = cnf.hidden_tautology_elimination()
        cnf = cnf.hidden_blocked_clause_elimination()
        return cnf

    def asymmetrics(self, cnf):
        cnf = cnf.asymmetric_subsumption_elimination()
        cnf = cnf.asymmetric_tautology_elimination()
        cnf = cnf.asymmetric_blocked_clause_elimination()
        return cnf

    def complete(self, cnf):

        cnf = cnf.asymmetric_subsumption_elimination()

        cnf = cnf.blocked_clause_elimination()
        cnf = cnf.tautology_elimination()
        cnf = cnf.subsumption_elimination()

        # cnf = cnf.hidden_tautology_elimination()
        cnf = cnf.asymmetric_tautology_elimination()

        # cnf = cnf.hidden_blocked_clause_elimination()
        cnf = cnf.asymmetric_blocked_clause_elimination()

        # cnf = cnf.hidden_subsumption_elimination()
        # cnf = cnf.asymmetric_subsumption_elimination()

        return cnf

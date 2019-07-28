import utils


class Clause:
    def __init__(self, variable_list):
        self.variable_list = variable_list
        self.size = len(self.variable_list)
        self.id = utils.create_id()

    def get_literals(self):
        return self.variable_list

    def get_literals_sub_sets(self):
        """
        Get all literals sub sets excluding the empty set
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

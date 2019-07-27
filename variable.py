class Variable:
    def __init__(self, variable_string):
        self.variable_int = int(variable_string)
        self.signal = 1
        if self.variable_int < 0:
            self.signal = -1
            self.variable_int = abs(self.variable_int)

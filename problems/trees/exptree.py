class Int:
    def __init__(self, n):
        self.n = n

    def is_const(self):
        return True

    def num_nodes(self):
        return 1

    def eval(self):
        return self.n

    def __str__(self):
        return str(self.n)


class Bool:
    def __init__(self, n):
        self.n = n

    def is_bool(self):
        return True

    def num_nodes(self):
        return 1

    def eval(self):
        return self.n

    def __str__(self):
        return str(self.n)


class BinOp:
    def __init__(self, op1, op2, operator):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator

    def is_const(self):
        return False

    def is_bool(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        if self.operator == '*':
            return op1_value * op2_value
        elif self.operator == '+':
            return op1_value + op2_value
        elif self.operator == '-':
            return op1_value - op2_value
        elif self.operator == '/':
            return op1_value / op2_value
        elif self.operator == 'and':
            return op1_value and op2_value
        elif self.operator == 'or':
            return op1_value or op2_value
        else:
            print("we should never see this")

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} {self.operator} {op2_str})"


class Abs:
    def __init__(self, op1):
        self.op1 = op1

    def is_const(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes()

    def eval(self):
        op1_value = self.op1.eval()
        return abs(op1_value)

    def __str__(self):
        op1_str = str(self.op1)

        return f"|{op1_str}|"


class Not:
    def __init__(self, op1):
        self.op1 = op1

    def is_bool(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes()

    def eval(self):
        op1_value = self.op1.eval()
        return not op1_value

    def __str__(self):
        op1_str = str(self.op1)

        return f"not {op1_str}"


if __name__ == "__main__":

    # Sample expression tree for (2 + (3 * 5))
    op1 = Int(2)
    op2 = BinOp(Int(-3), Int(5), "*")
    op3 = Abs(op2)
    expt = BinOp(op1, op3, "/")

    op1 = Bool(True)
    op2 = BinOp(Bool(False), Bool(True), "or")
    op3 = Not(op2)
    expt2 = BinOp(op1, op3, "and")

    print(f"{expt2} = {expt2.eval()}")

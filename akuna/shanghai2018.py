class SumUnit(object):
    unit_name = None
    input0 = None
    input1 = None
    output0 = None

    def __init__(self, unit_name, input0, input1, output0):
        self.unit_name = unit_name
        self.input0 = input0
        self.input1 = input1
        self.output0 = output0

    def execute(self):
        if self.input0.val and self.input1.val:
            res = int(self.input0.val) + int(self.input1.val)
            self.output0.val = res
            self.output0.from_.val = res
            self.output0.to.val = res


class NegateUnit(object):
    unit_name = None
    input0 = None
    output0 = None

    def __init__(self, unit_name, input0, output0):
        self.unit_name = unit_name
        self.input0 = input0
        self.output0 = output0

    def execute(self):
        self.output0.val = 0 - self.input0.val

class MaxUnit(object):
    unit_name = None
    input0 = None
    input1 = None
    output0 = None

    def __init__(self, unit_name, input0, input1, output0):
        self.unit_name = unit_name
        self.input0 = input0
        self.input1 = input1
        self.output0 = output0

    def execute(self):
        if self.input0.val and self.input1.val:
            self.output0.val = max(self.input0.val, self.input1.val)

class MinUnit(object):
    unit_name = None
    input0 = None
    input1 = None
    output0 = None

    def __init__(self, unit_name, input0, input1, output0):
        self.unit_name = unit_name
        self.input0 = input0
        self.input1 = input1
        self.output0 = output0

    def execute(self):
        if self.input0.val and self.input1.val:
            self.output0.val = min(self.input0.val, self.input1.val)

class MulUnit(object):
    unit_name = None
    input0 = None
    input1 = None
    output0 = None

    def __init__(self, unit_name, input0, input1, output0):
        self.unit_name = unit_name
        self.input0 = input0
        self.input1 = input1
        self.output0 = output0

    def execute(self):
        if self.input0.val and self.input1.val:
            self.output0.val = self.input0.val * self.input1.val

class Pipe(object):
    name = None
    from_ = None
    to = None
    val = None

    def __init__(self, name, from_, to):
        self.name = name
        self.from_ = from_
        self.to = to

class ValNode(object):
    name = None
    val = None

    def __init__(self, name, val):
        self.name = name
        self.val = val

class UnitNode(object):
    name = None
    dir = None
    val = None

    def __init__(self, name, dir, val):
        self.name = name
        self.dir = dir
        self.val = val

class ResultNode(object):
    name = None
    val = None

    def __init__(self, name):
        self.name = name

class InputParser(object):
    val_objs = []
    input_node = {}
    node_pipe = {}
    pipe_unit = {}
    res = None
    prev_res = None
    units = {}
    conn_funcs = []
    flow = []
    inputs = None
    res_node = None

    def process(self):
        units_num = self.get_section_title_line()

        for i in range(units_num):
            name, type_ = self.get_section_internal_line()
            if self.unit_callback_:
                self.unit_callback_(name, type_)

        inputs_num = self.get_section_title_line()
        if self.input_callback_:
            self.input_callback_(inputs_num)

        connections_num = self.get_section_title_line()

        for i in range(connections_num):
            from_, to = self.get_section_internal_line()
            assert from_ != 'result'
            from_strs = from_.split('/')
            assert len(from_strs) >= 2
            to_strs = to.split('/')
            """
            TODO: to_strs instead of from_strs?
            """
            assert len(to_strs) >= 1
            second = '' if from_strs[0] == "input" else from_strs[1]
            third = from_strs[1] if from_strs[0] == "input" else from_strs[2]
            fifth = ''
            sixth = ''
            """
            TODO: if to_strs[0] == 'input' then we are passing the val
            to another unit
            """
            if to_strs[0] == 'input':
                sixth = to_strs[1]
            elif to_strs[0] != 'result':
                fifth = to_strs[1]
                sixth = to_strs[2]

            if self.connection_callback_:
                self.connection_callback_(from_strs[0], second,
                    third, to_strs[0], fifth, sixth)

        values_num = self.get_section_title_line()

        print('\n')
        for i in range(values_num):
            input_, value = self.get_section_internal_line()
            strs = input_.split('/')
            assert len(strs) == 2
            if self.value_callback_(strs[0], strs[1], value):
                print(self.res)

    def split(self, s, delim, result):
        for x in s.split(delim):
            result.append(x)

    def split(self, s, delim):
        return s.split(delim)

    def get_section_title_line(self):
        line = input()
        words = line.split(' ')
        assert len(words) == 2
        return int(words[1])

    def get_section_internal_line(self):
        line = input()
        words = line.split(' ')
        assert len(words) == 3
        return words[0], words[2]

    def unit_callback_(self, s1, s2):
        s_unit = {
            'sum': SumUnit(s1, None, None, None),
            'negate': NegateUnit(s1, None, None),
            'max': MaxUnit(s1, None, None, None),
            'min': MinUnit(s1, None, None, None),
            'mul': MulUnit(s1, None, None, None)
        }

        unit = s_unit[s2]
        self.units[s1] = unit

    def input_callback_(self, n):
        self.inputs = [None for i in range(n)]

    def connection_callback_(self, s1, s2, s3, s4, s5, s6):
        unit0, unit1 = None, None

        if not s2:
            from_ = ValNode(s1 + s3, None)
        else:
            from_ = UnitNode(s1, s2, s3)
        if s4 == 'result':
            to = ResultNode(s4)
            self.res_node = to
        else:
            to = UnitNode(s4, s5, s6)

        pipe = Pipe(from_.name + ' ' + to.name, from_, to)
        """
        two types of pipes val --> unit or unit --> unit

        result

        check unit structure --> input nodes or class?
        """
        # only input pipe b/c unit --> input pipe doesn't make sense
        if type(from_) == ValNode and type(to) == UnitNode:
            unit0 = self.units[s4]
            self.input_node[from_.name[5:]] = from_
            if s6 == '0':
                unit0.input0 = pipe
            else:
                unit0.input1 = pipe
        elif type(from_) == UnitNode and type(to) == UnitNode:
            unit0 = self.units[s1]
            unit1 = self.units[s4]
            """unit0 output to unit1 input"""
            if s2 == 'out':
                unit0.output0 = pipe
                if s6 == '0':
                    unit1.input0 = pipe
                else:
                    unit1.input1 = pipe
        #result
        elif type(from_) == UnitNode and type(to) == ResultNode:
            unit0 = self.units[s1]
            unit0.output0 = pipe

        if unit0 and unit1:
            if unit0 not in self.flow:
                self.flow.append(unit0)
            if unit1 not in self.flow:
                self.flow.append(unit1)
            self.pipe_unit[pipe] = unit0
            self.pipe_unit[pipe] = unit1
        else:
            if unit0 not in self.flow:
                self.flow.append(unit0)
            self.pipe_unit[pipe] = unit0
        # only need from_ : pipe mapping
        self.node_pipe[pipe.from_] = pipe
        self.node_pipe[pipe.to] = pipe

    def value_callback_(self, s1, s2, s3):
        """
        mapping:
        input --> node
        node --> pipe
        pipe --> unit? run unit and subsequent units and see
        if res is diff
        [unit0, unit1, unit2, unit3, ...]
        """
        node = self.input_node[s2]
        node.val = s3
        pipe = self.node_pipe[node]
        pipe.val = s3
        unit = self.pipe_unit[pipe]
        i = self.flow.index(unit)
        self.prev_res = self.res
        for j in range(i, len(self.flow)):
            self.flow[j].execute()
        self.res = self.res_node.val
        if self.res != self.prev_res:
            return True

if __name__ == '__main__':
    ip = InputParser()
    ip.process()


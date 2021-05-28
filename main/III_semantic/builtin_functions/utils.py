from main.III_semantic.data_types.array_data.numeric_data.decimal_data.double import Double


def creator_function_generator(value):
    def matrix_generator(argv):
        if len(argv) == 0:
            return Double([value])
        if len(argv) == 1:
            arg = argv[0]
            if arg.size == (1, 1):
                m = int(arg[0])
                n = int(arg[0])
            if arg.size == (1, 2):
                m = int(arg[0])
                n = int(arg[1])
            return Double([value] * m * n, size=(m, n))
        if len(argv) == 2:
            m = int(argv[0][0])
            n = int(argv[1][0])
            return Double([value] * m * n, size=(m, n))
    return matrix_generator

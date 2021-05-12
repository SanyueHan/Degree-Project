"""
https://ww2.mathworks.cn/help/matlab/control-flow.html?s_tid=CRUX_lftnav
"""


from utils.random_statements import *


DIRECTORY = '../../test_cases/language_fundamentals/v_loops_and_conditional_statements/'


if __name__ == "__main__":
    with open(DIRECTORY+"test_1_if_else.m", 'w') as file_1:
        generator = RandomStatementGenerator()
        file_1.write(generator.random_if_else_statement())
    with open(DIRECTORY+"test_2_switch_case.m", 'w') as file_2:
        generator = RandomStatementGenerator()
        file_2.write(generator.random_switch_case_statement())
    with open(DIRECTORY+"test_3_for.m", 'w') as file_3:
        generator = RandomStatementGenerator()
        file_3.write(generator.random_for_statement())
    with open(DIRECTORY+"test_4_while.m", 'w') as file_4:
        generator = RandomStatementGenerator()
        file_4.write(generator.random_while_statement())
    with open(DIRECTORY+"test_total.m", 'w') as file_t:
        generator = RandomStatementGenerator(stmt=2, exp=3)
        file_t.write(''.join(generator.random_statement_list(number=200)))

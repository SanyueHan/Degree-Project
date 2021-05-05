"""
https://ww2.mathworks.cn/help/matlab/control-flow.html?s_tid=CRUX_lftnav
"""


from utils.random_statements import *


DIRECTORY = '../../test_cases/language_fundamentals/v_loops_and_conditional_statements/'


if __name__ == "__main__":
    with open(DIRECTORY+"test_1_if_else.m", 'w') as file_1:
        file_1.write(random_if_else_statement())
    with open(DIRECTORY+"test_2_switch_case.m", 'w') as file_2:
        file_2.write(random_switch_case_statement())
    with open(DIRECTORY+"test_3_for.m", 'w') as file_3:
        file_3.write(random_for_statement())
    with open(DIRECTORY+"test_4_while.m", 'w') as file_4:
        file_4.write(random_while_statement())
    with open(DIRECTORY+"test_total.m", 'w') as file_t:
        file_t.write(''.join(random_statement_list(number=100)))

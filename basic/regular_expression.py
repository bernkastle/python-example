import re


def tel_reg():
    """
    匹配手机号码和座机号码
    :return:
    """
    pattern = re.compile(r'(^[8,6]\d{7}$)|(^0[1-9]\d{1,2}\\d{7,8}$)|(^1[3456789]\d{9}$)')
    m1 = pattern.match('13500000000')
    m2 = pattern.match('83210000')
    print(m1, m2)

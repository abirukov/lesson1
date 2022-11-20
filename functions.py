def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'

sum_result = get_summ('Learn', 'python')
print(sum_result)
print(sum_result.upper())

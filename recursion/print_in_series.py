def print_series(str):
    if len(str) ==0:
        return ''
    return str[0]+ print_series(str[:-1])

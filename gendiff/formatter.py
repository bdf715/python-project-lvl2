def formatter(data):
    result = '{\n'
    for item in data:
        name = item['name']
        value = item['value']
        sign = item['sign']
        result += ' {0} {1}: {2}\n'.format(sign, name, value)
    result += '}'
    return result

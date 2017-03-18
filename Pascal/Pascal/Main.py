from operators import *

# path = 'C:\\Users\\mired\\Desktop\\Program\\Pascal\\Programs\\inttest\\Program1.pas'
path = str(input('Enter location of file: '))

pascal = open(path, 'r')

code = pascal.read()
code_lines = code.split(sep='\n')[1:-1]
code_lines.remove('')
for n in range(len(code_lines)):
    code_lines[n] = code_lines[n].strip(' ;')

for line in code_lines:
    if line == 'begin':
        break
    line = line.split(sep=': ')
    for variable in line[0].split(sep=', '):
        for var_type in var_types.keys():
            if line[1] == var_type:
                variables[variable] = var_types[var_type]

for line in code_lines[code_lines.index('begin')+1:]:
    for function_name in functions.keys():
        if line.startswith(function_name):
            argument = line.replace(function_name, '', 1)[:-1]
            functions[function_name](argument)

pascal.close()

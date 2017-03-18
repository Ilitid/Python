def write(arg):
    for part in arg.split(sep=', '):
        if part[0] == '\'':
            print(part.strip('\''), end='')
        else:
            print(variables[part], end='')

def writeln(arg):
    for part in arg.split(sep=', '):
        if part[0] == '\'':
            print(part.strip('\''), end='')
        else:
            print(variables[part], end='')
    print()

def read(arg):
    variables[arg] = input()


functions = {
    'read(': read,
    'write(': write,
    'writeln(': writeln
}

variables = {
    'pi': 3.14159
}

var_types = {
    'integer': 0,
    'longint': 0,
    'real': 0.0,
    'string': '',
    'boolean': False
}

global_variables = {}


def set_var(name, value):
    global_variables[name] = value


def get_var(name):
    return global_variables[name]

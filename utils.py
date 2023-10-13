# utils.py

function_dict = {}

def execute_function(code, function_name, somestring):
    try:
        locals_dict = {"somestring": somestring}
        exec(code, globals(), locals_dict)
    except Exception as e:
        print(f"Error executing function '{function_name}': {str(e)}")

def register_function(name, function):
    global function_dict
    function_dict[name.lower()] = function

def get_function(name):
    global function_dict
    return function_dict.get(name.lower())


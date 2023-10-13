# hello_world_module.py
from credentials import get_credentials
from connection_manager import connect_to_api, parse_response
from utils import execute_function

credentials = get_credentials()
url = credentials.get('URL')
headers = {
    "X-Parse-Application-Id": credentials.get('X-Parse-Application-Id'),
    "X-Parse-REST-API-Key": credentials.get('X-Parse-REST-API-Key'),
    'Content-Type': 'application/json'
}

response = connect_to_api(url, headers)

if response:
    results = parse_response(response)

    if results:
        for result in results:
            function_name = result.get("Function")
            code_to_execute = result.get("PythonCode")
            somestring = " world"  # Define the somestring variable with your desired value
            
            if function_name == "Hello" and code_to_execute:
                execute_function(code_to_execute, function_name, somestring)
                
    else:
        print("No 'results' found in the API response.")

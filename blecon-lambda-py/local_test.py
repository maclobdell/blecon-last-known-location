#todo: add license

from lambda_function import *
import json

def main():

    print("LAMBDA TEST")

    filename = "test.json"
    event = json.loads(read_file(filename))
    return_value = lambda_handler(event, None)
    print(return_value)

def read_file(filename):

    with open (filename, "r") as f:    
        file_data = f.read() 
        f.close()
    return file_data

if __name__ == '__main__':
    main()


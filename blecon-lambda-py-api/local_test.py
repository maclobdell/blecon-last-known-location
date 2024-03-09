from lambda_function import *

def main():

    print("LAMBDA TEST")

    #For some reason when I run the actual lamda the body was coming out as a string instead of an ojbect, but when I run the lambda test or run it loacally, it comes out as an object!!!
    # So the local test does not work right now

    filename = "api-event.json"
    event_str = read_file(filename)
    print(type(event_str))
    print(event_str)

    event = json.loads(event_str)

    return_value = lambda_handler(event, None)
    print(return_value)

def read_file(filename):

    with open (filename, "r") as f:    
        file_data = f.read() 
        f.close()
    return file_data

if __name__ == '__main__':
    main()


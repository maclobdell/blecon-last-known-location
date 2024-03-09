import requests

def main():

    print("API TEST")

#TODO - figure out if the Device ID changes!?

    request_data = {'device_id':'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx'}
    header_data =  {'Content-Type': 'application/json'}

    r = requests.post('https://xxxxxxxx.execute-api.us-east-2.amazonaws.com/default/blecon-locator-api', headers=header_data, json=request_data)

    print(r.status_code)
    print(r.json())

if __name__ == '__main__':
    main()


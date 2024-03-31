import requests

endpoint_url = "https://api.spacexdata.com/v5/launches/latest"

response = requests.get(endpoint_url)

if response.status_code == 200:
    print("Status Code: ",response.status_code)
    print("Response Content: ")

    data = response.json()

    mission_name = data['name']
    flight_number = data["flight_number"]
    date = data["date_utc"]
    land_success = data["cores"][0]["landing_success"]
    land_type = data["cores"][0]["landing_type"]
    mission_success_status = data["success"]
    details = data["details"]


    print(f"Name of the Mission: {mission_name}")
    print(f"Flight Number: {flight_number}")
    print(f"Date of the Mission: {date}")
    print(f"Was the Landing Successful: {land_success}")
    print(f"Type of Landing: {land_type}")
    print(f"Was the Mission Successful: {mission_success_status}")
    print(f"\nDetails of the Mission: {details if details else "No Details Available"}")
else:
    print(f"Invalid Process. There is an error in obtaining data. Status code: ",response.status_code)
    





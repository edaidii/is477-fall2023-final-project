#importing necessary 
import requests
import hashlib
import os

#hashes computed manually
car_zip_hash = '1559d51dcf327f4f8c71b711ceed7fd95a382fc8d8e1998667f4f23b82860403'

#downloading the necessary datafiles using their url
car_url = 'https://archive.ics.uci.edu/static/public/19/car+evaluation.zip'

#downloading the car+evaluation.zip data and calculating SHA-256 using the hashlib
response = requests.get(car_url)
#testing if there will be a download error
if response.status_code == 200:
    print ('200 Error')

with open('car+evaluation.zip', mode='wb') as f:
    f.write(response.content)
#made an additional revision from the first submission to properly match and correct the variable filename
filename_car = 'car+evaluation.zip'
with open(filename_car, mode='rb') as f:
    data = f.read()
    sha256hash_car = hashlib.sha256(data).hexdigest()

#determining if the hashes match up
#made an additional revision from the first submission to properly run the and operator by adding parentheses
if car_zip_hash != sha256hash_car:
    print("Computed hash does not match expected hash")
else:
    print("Computed hash matches expected hash")

#hashes computed manually
car_csv_hash = 'b703a9ac69f11e64ce8c223c0a40de4d2e9d769f7fb20be5f8f2e8a619893d83'

#made an additional revision from the first submission to properly match and correct the variable filename
filename_car_csv = r'/Users/edward/is477-fall2023-final-project/data/car+evaluation/car.csv'
with open(filename_car_csv, mode='rb') as f:
    data = f.read()
    sha256hash_car_csv = hashlib.sha256(data).hexdigest()

#determining if the hashes match up
#made an additional revision from the first submission to properly run the and operator by adding parentheses
if car_csv_hash != sha256hash_car_csv:
    print("Computed hash does not match expected hash")
else:
    print("Computed hash matches expected hash")
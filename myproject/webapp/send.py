import requests
headers={ }
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk2Njk4MDYxLCJqdGkiOiI5ZjhjMzU4M2Y3Y2M0NDM2YjQ3NTViNmE3ZWRhOWJhOSIsInVzZXJfaWQiOjF9.8uDYBbtSvgF-ecPMY08IZQvL2cGWL-gOTXtIckInwxQ'
r = requests.get('http://127.0.0.1:8000/teacher/', headers=headers)
print(r.text)
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk2Njk4MDYxLCJqdGkiOiI5ZjhjMzU4M2Y3Y2M0NDM2YjQ3NTViNmE3ZWRhOWJhOSIsInVzZXJfaWQiOjF9.8uDYBbtSvgF-ecPMY08IZQvL2cGWL-gOTXtIckInwxQ'
r = requests.get('http://127.0.0.1:8000/student/', headers=headers)
print(r.text)
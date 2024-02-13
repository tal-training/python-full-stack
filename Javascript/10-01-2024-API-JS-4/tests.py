import requests
import json

def test_range():  
     data={"low":10, "high":20}
     my_json=json.dumps(data)
     r=requests.post("http://127.0.0.1:5000/api/guess/range", data=my_json, headers={"Content-type":"application/json"}).json()
     return data['low'] <= r['number'] <= data['high']

def test_guess():
     my_number=5
     number=requests.get("http://127.0.0.1:5000/api/test/number").json()
     result=requests.post("http://127.0.0.1:5000/api/guess", data=json.dumps({"number":my_number})).json()
     if number==my_number:
        return result["result"]=="win"
     if number<my_number:
        return result["result"]=="low"
     else:
        return result["result"]=="high"
         

print(test_range())
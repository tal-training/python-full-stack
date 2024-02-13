import requests

def test_api_to100():
    for i in range(100):
        assert 1 < requests.get(url="http://127.0.0.1:5000/to100").json()["result"] < 100 

def test_api_smaller100():
    num=100
    assert requests.get(url=f"http://127.0.0.1:5000/smaller100?num={num}").json()["result"]=="ERROR"  
    assert requests.get(url=f"http://127.0.0.1:5000/smaller100?num={99}").json()["result"]=="OK"  
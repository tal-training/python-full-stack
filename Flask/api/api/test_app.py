import requests

def test_echo():
    val="aaaa"
    url=f"http://127.0.0.1:5000/echo?input={val}"
    r=requests.get(url=url)
    assert val==r.json()["result"]
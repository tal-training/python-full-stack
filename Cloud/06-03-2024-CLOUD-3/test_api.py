import app
import json
import datetime

def test_register_visit():
    app.register_visit()
    visits_num_before=len(json.loads(app.test()))
    app.register_visit()
    visits_num_after=len(json.loads(app.test()))
    assert visits_num_after==visits_num_before+1

def test_status():
    assert json.loads(app.register_visit())["visit registered"]=="ok"


def test_date_valid():
    app.register_visit()
    assert json.loads(app.test())[-1][1]==str(datetime.date.today())
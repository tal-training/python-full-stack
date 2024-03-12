from functions import echo, vat, add, to100, smaller100, str_len, str_starts

def test_echo():
    assert echo(1)==1, "echo should be 1"

def test_vat():
    assert vat(10)==str(10*1.17)    
    assert vat("10")==str(10*1.17)
    assert type(vat(10))==str

# write unit test for add
    
def test_add():
    assert add(1,2)==3

def test_to100():
    for i in range(1000):
        assert 1 < to100() < 100 

def test_smaller100():
    num1="99"
    num2=100
    not_num="sfdsdfsfg"
    assert smaller100(num1)=="OK"
    assert smaller100(num2)=="ERROR"    
    assert smaller100(not_num)=="ERROR"

def test_str_len():
    s1="asdsa"
    s2="sdasdsaadasd"
    s3=1111111
    assert str_len(s1)=="OK"
    assert str_len(s2)=="ERROR"
    assert str_len(s3)=="ERROR"

def test_str_starts():
    s1="Alex"
    s2="Bob"
    assert str_starts(s1)=="OK"
    assert str_starts(s2)=="ERROR"

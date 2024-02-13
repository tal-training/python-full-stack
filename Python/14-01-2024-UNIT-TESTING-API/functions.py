import random

def echo(num):
    return num

def vat(num):
    return str(int(num)*1.17)

def add(a,b):
    return a+b

def to100():
    return random.randint(2,99)

def smaller100(num:int):
    try:
        if int(num)<100:
            return "OK"
        else:
            return "ERROR"
    except:
        return "ERROR"

def str_len(s:str):
    try:
        if len(s)==5:
            return "OK"
        else:
            return "ERROR"
    except:
        return "ERROR"

def str_starts(s:str):
    try:
        if s[:1]=="A":
            return "OK"
        else:
            return "ERROR"
    except:
        return "ERROR"
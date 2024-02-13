import time

class Car:
    def __init__(self, speed=0, rpm=1):
        self.speed=speed
        self.rpm=rpm
        self.fuel=100
        self.low_fuel=False

    def set_rpm(self, num):
        self.rpm=num
        self.speed+=num

    def accelerate(self, amount):
        self.speed+=amount
        self.rpm*=10
        self.fuel-=10
        if self.fuel<20:
            self.low_fuel=True
        if fuel==0:
            self.set_rpm(-10)

while True:
    time.sleep(1)
    



car1=Car(speed=0, rpm=1)
car2=Car(speed=20, rpm=20)
car1.accelerate(100)
print(car1.speed)
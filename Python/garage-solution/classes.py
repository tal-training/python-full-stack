class Address:
    def __init__(self, country:str="israel", city:str="haifa") -> None:
        self.country=country  
        self.city=city


class Car:
    def __init__(self, name="name", year="year", color="color", license="license", owner="owner", visit_date="", service_date="", address=Address()) -> None:
        self.name=name
        self.year=year
        self.color=color
        self.license=license
        self.owner=owner
        self.visit_date=visit_date
        self.service_date=service_date
        self.address=address

    def __repr__(self) -> str:
        return f"{self.name}:{self.license}"

    def __str__(self):
        return f"{self.name}\t{self.year}\t{self.color}\t{self.license}\t{self.owner}\t{self.visit_date}\t{self.service_date}\t{self.address.city}"


    
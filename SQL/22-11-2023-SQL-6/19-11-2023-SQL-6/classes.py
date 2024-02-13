class Company:
    def __init__(self, name, company_type) -> None:
        self.name=name
        self.type=company_type


class Product:
    def __init__(self, name:str="", price:str="", image:str="", company:Company=None) -> None:
        self.pid=0
        self.name=name
        self.price=price
        self.image=image
        self.company=company    # composition

# class Shoe(Product):  # inheritance

# class Car(Product)    # inheritance



class Company:
    def __init__(self, name, company_type) -> None:
        self.name=name
        self.type=company_type
        self.products=[]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Product:
    def __init__(self, name:str="", price:str="", image:str="", company:Company=None, company_id=0, pid=0) -> None:
        self.pid=pid
        self.name=name
        self.price=price
        self.image=image
        self.company=company    # composition
    
    def __str__(self) -> str:
        return self.name

    
class Cart:
    def __init__(self) -> None:
        self.products=[]

    def add(self, product:Product):
        self.products.append(product)

    def __repr__(self) -> str:
        return str(self.products)
        
    def __str__(self) -> str:
        return str(self.products)


# class Shoe(Product):  # inheritance

# class Car(Product)    # inheritance



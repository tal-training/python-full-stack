class Contact:
    country="Israel"
    def __init__(self):
        name=""
        phone=""
        email="ddddd"
    
    def print_name(self):
        print(self.name)


tal=Contact()
tal.name="tal"
tal.phone="023-8903243"

tal.print_name()
tal.print_hi()
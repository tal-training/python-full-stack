class Contact:
    def __init__(self, friend, name="name", phone="phone") -> None:
        self.name=name
        self.phone=phone

    def __repr__(self) -> str:
        return f"{self.name}:{self.phone}"
contacts1={
    "tal":{
    "name":"tal",
    "phone":"052-1111111",
    "email":"tal@tal.com"
    },
    "gal":{
    "name":"gal",
    "phone":"053-2222222",
    "email":"gal@gal.com"
    }
}

contacts2={
    "mal":{
    "name":"mal",
    "phone":"052-1111111",
    "email":"tal@tal.com"
    },
    "yal":{
    "name":"yal",
    "phone":"053-2222222",
    "email":"gal@gal.com"
    }
}

def get_phone(contacts_dict, name):
    for contact in contacts_dict.values():
        if contact["name"]==name:
            return contact["phone"]
        else:
            return "lo kayam"

print(get_phone(contacts2, "tal111"))

# כתבו פונקציה דומה שמחזירה את המייל

def get_mail(contacts_dict, name):
    for contact in contacts_dict.values():
        if contact["name"]==name:
            return contact["email"]

print(get_mail(contacts2, "yal"))


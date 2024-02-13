contacts=[
    {
    "name":"tal",
    "phone":"052-1111111",
    "email":"tal@tal.com"
    },
    {
    "name":"gal",
    "phone":"053-2222222",
    "email":"gal@gal.com"
    },
    {
    "name":"yal",
    "phone":"054-444444",
    "email":"yal@yal.com"
    }
]

def format_dict(dict_item):
    return ','.join(dict_item.values())    

for contact in contacts:
    print(format_dict(contact))
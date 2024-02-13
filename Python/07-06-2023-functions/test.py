contacts={"tal":{"name":"tal","phone":"052-1111111","email":"tal@tal.com"},
"gal":{"name":"gal","phone":"053-2222222","email":"gal@gal.com"}}

for internal_dict in contacts.values():
    for key in internal_dict:
        print(internal_dict.values())


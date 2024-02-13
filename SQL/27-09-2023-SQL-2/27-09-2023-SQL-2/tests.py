from decimal import Decimal
import datetime

l=['Health and safety adviser', 'Everett and Sons', '794-84-5954', '6649 Mark Meadow Suite 542\nChanchester, PR 94460', (Decimal('8.7101835'), Decimal('32.059894')), 'O-', ['http://baldwin-jones.biz/', 'http://www.munoz-thompson.org/', 'http://www.hanson-wright.com/', 'http://www.williams.com/'], 'qlloyd', 'Julie Campbell', 'F', '758 Green Glen Suite 778\nShannonmouth, NH 45103', 'ffernandez@yahoo.com', datetime.date(1991, 1, 31)]


for i in l:
    print(str(i))
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


with open('numbers.txt', 'r') as f:
    numbers = f.readlines()

print(type(numbers))


def checknumber(number):
    country = ''
    ch_number = phonenumbers.parse(number, "CH")
    country += geocoder.description_for_number(ch_number, "en")

    telco = ''
    service_number = phonenumbers.parse(number, 'RO')
    telco += carrier.name_for_number(service_number, 'en')
    
    line = f'{number} | {country} | {telco}'
    
    with open('checkednumbers.txt', 'a+') as f:
        f.write(line)
        f.write('\n')

for number in numbers:
    number = number.strip('\n')
    checknumber(number)



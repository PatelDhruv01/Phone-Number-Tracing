import phonenumbers as pn
from phonenumbers import timezone, geocoder, carrier

number=input("Enter your number(with country code +__): ")
phone=pn.parse(number)
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone, "en")  # en for displaying company name in English
reg=geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(carr)
print(reg)
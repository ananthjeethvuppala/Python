letter='Hey My Name is {} and I am from {}'
country='India'
name='Ananth'

print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")#For displaying the string as it is

txt = "For only {price:.2f} dollars!"#Returns upto 2 Decimal digits
print(txt.format(price = 49.0994599))

price=49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(type(txt))

print(f"{2*30}")
print(type(f"{2*30}"))
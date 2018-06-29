message = "One of Python's strengths is its diverse community."
print(message)

#Personal Mesage
ryan = "Hello Ryan, do you want to become good at Financial Engineering using Python and R"
print(ryan)

#Name Case
name = "chris lynch"
print(name.upper())
print(name.lower())
print(name.title())

#Famous Quote
quote = "\tSteve Jobs once said, 'The ones who are crazy enough to think \n\tthat they can change the world \n\tare the ones who do.'"
print(quote)

#Famous Quote 2
famous_person = "Steve Jobs"
message = "\t{} once said, 'The ones who are crazy enough to think \n\tthat they can change the world \n\tare the ones who do.'".format(famous_person)
print(message)

#Stripping names
x = "\tRyan \nMcGovern"
print(x)
print(x.lstrip())
print(x.rstrip())
print(x.strip())

#Avoiding type errors
age = 21
y = "Happy " + str(age) + "st Birthday!" #Use str to covert type!!!
print(y)

#Number 8
print(2+6)
print(12-4)
print(4*2)
print(int(16/2))

#Favorite number: this is exercise 2-10
num = 21
print("My favorite number is " + str(num) + "!" )

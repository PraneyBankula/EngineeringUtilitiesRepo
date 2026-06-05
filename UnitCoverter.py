unit = input("Are you in farenheit or celsius? (c/f): ")
while unit != "c" and unit != "f":
    print("That is not a valid option, please try again")
    unit = input("Are you in farenheit or celsius? (c/f): ")
if unit == "c":
    celsius = int(input("How many degrees celsius? "))
    fahrenheit  = (celsius * (9/5)) + 32
    print(str(celsius) + " degrees celsius is " + str(fahrenheit) + " degrees fahrenheit")
elif unit == "f":
    fahrenheit = int(input("How many degrees fahrenheit"))
    celsius = (fahrenheit -32) * 5/9
    print(str(fahrenheit) + " degrees fahrenheit is " + str(celsius) + " degrees celsius")
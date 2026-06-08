colors = {
    "black" : 0,
    "brown" : 1,
    "red" : 2,
    "orange" : 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet" : 7,
    "grey" : 8,
    "white" : 9

}
name = input("What's your name?")
print("Hello " + name + " this is a 3 band resistor calculator")
firstBand = input("First Band: ").lower()
secondBand = input("Second Band: ").lower()
thirdBand = input("Third Band: ").lower()
calculation = (colors[firstBand] * 10 + colors[secondBand]) * pow(10, colors[thirdBand])
print("the resistor of a band consisting of the colors " + firstBand + ", " + secondBand + ", " + "and " + thirdBand + " is " + str(calculation) + " ohms")
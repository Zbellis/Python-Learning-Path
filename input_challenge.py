# ask user to input mph and convert to mph

def to_mph():
    speedKph = input("Enter your speed in Kilometers per hour: ")

    int_speedKph = int(speedKph)
    
    speedMph = int_speedKph / 1.609

    print("Your speed in mph is: {} and in kph is: {}".format(speedMph, int_speedKph))


to_mph()

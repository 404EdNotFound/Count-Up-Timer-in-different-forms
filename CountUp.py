from tkinter import *
import time

# max_seconds = 10
startTime = elapsedTime = 0

window = Tk()
window.title("Count-up Stopwatch")

def runningTimer():
    global startTime
    startTime = time.time() - elapsedTime
    updateDisplay()

def romanNumeralConversion(time):
    textString = char = ""
    
    romanNumeralsDictionary = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"} #Dictionary used for cleaner storage so that each value is mapped to specific key
    comparisonNumber = int(time) #Int Casting from Float
    
    #Cleaner Approach for Converting Numbers into Roman Numerals
    for key in romanNumeralsDictionary:
        while comparisonNumber >= key:
            char = romanNumeralsDictionary[key]
            textString += char
            comparisonNumber -= key
            
    return textString

#Binary Convetion from Denary
def binaryConverter(time):
    textString = ""
    rootPower = 1
    decimalPrefix = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1] # Static Approach for setting prefixes
    dynamicDecialPrefix = []
    
    comparisonNumber = int(time)
    
    while rootPower * 2 <= comparisonNumber: #Needed help with setting a dynamic approach for conversion to binary numbers
        rootPower *= 2
    
    while rootPower > 0:
        dynamicDecialPrefix.append(rootPower)
        rootPower //= 2

    for number in dynamicDecialPrefix:
        if comparisonNumber >= number:
            textString += "1"
            comparisonNumber -= number
        
        else:
            textString += "0"
    return textString

def hexadecimalConverter(binaryNumber):
    paddedBinaryNumber = ""
    hexMap = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7", "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"}
    hexTextString = ""
    
    if len(binaryNumber) % 4 != 0:
        paddedBinaryNumber = ("0" * (4 - (len(binaryNumber) % 4))) + binaryNumber
    
    else: paddedBinaryNumber = binaryNumber
    
    for count in range(0, len(paddedBinaryNumber), 4):
        slice = paddedBinaryNumber[count:count+4]
        hexTextString += hexMap[slice]
    
    return hexTextString

def updateDisplay():
    global elapsedTime
    elapsedTime = time.time() - startTime
    hours = minutes = seconds = 0
    romanNumerals = timeFormat = ""

    # Used for converting time
    # if int(elapsedTime) <= max_seconds:
    #     minutes, seconds = divmod(int(elapsedTime), 60)
    #     hours, minutes = divmod(int(minutes), 60)
    
    minutes, seconds = divmod(int(elapsedTime), 60)
    hours, minutes = divmod(int(minutes), 60)
    
    if hours > 0:
        timeFormat = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    else:
        timeFormat = f"{int(minutes):02}:{int(seconds):02}"
        
    romanNumerals = romanNumeralConversion(elapsedTime)
    binaryNumber = binaryConverter(elapsedTime)
    hexadecimalNumber = hexadecimalConverter(binaryNumber)

    romanNumeralsLabel.config(text = romanNumerals)
    binaryConverterLabel.config(text = binaryNumber)
    hexadecimalConverterLabel.config(text = hexadecimalNumber)
    stopwatchLabel.config(text = timeFormat)
    stopwatch_seconds_Label.config(text = int(elapsedTime))
    
    window.after(1, updateDisplay)

window.config(background = "black")
backgroundFrame = Frame(window, background = "black")
stopwatchLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans MS", 40, "bold"), text = "00:00:00")
stopwatch_seconds_Label = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans MS", 40, "bold"))
romanNumeralsLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans Ms", 40, "bold"))
binaryConverterLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans Ms", 40, "bold"))
hexadecimalConverterLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans Ms", 40, "bold"))

runningTimer()
backgroundFrame.pack()
stopwatchLabel.pack()
stopwatch_seconds_Label.pack()
romanNumeralsLabel.pack()
binaryConverterLabel.pack()
hexadecimalConverterLabel.pack()

window.mainloop()
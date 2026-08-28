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
    decimalPrefix = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    
    comparisonNumber = int(time)
    
    for number in decimalPrefix:
        if comparisonNumber >= number:
            textString += "1"
            comparisonNumber -= number
        
        else:
            textString += "0"
    return textString

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

    romanNumeralsLabel.config(text = romanNumerals)
    binaryConverterLabel.config(text = binaryNumber)
    stopwatchLabel.config(text = timeFormat)
    
    window.after(1000, updateDisplay)

window.config(background = "black")
backgroundFrame = Frame(window, background = "black")
stopwatchLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans MS", 40, "bold"), text = "00:00:00")
romanNumeralsLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans Ms", 40, "bold"))
binaryConverterLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans Ms", 40, "bold"))

runningTimer()
backgroundFrame.pack()
stopwatchLabel.pack()
romanNumeralsLabel.pack()
binaryConverterLabel.pack()

window.mainloop()
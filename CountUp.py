from tkinter import *
import time

max_seconds = 10
startTime = elapsedTime = 0

window = Tk()
window.title("Count-up Stopwatch")

def runningTimer():
    global startTime
    startTime = time.time() - elapsedTime
    updateDisplay()

def romanNumeralConversion(time):
    textString = ""
    char = ""
    romanNumeralPairs = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    comparisonNumber = int(time)

    for pair in romanNumeralPairs:
        while comparisonNumber >= pair[0]:
            char = pair[1]
            textString += char
            comparisonNumber -= pair[0]
    
    # Old Approach of conversion with Roman Numerals       
    # while (comparisonNumber > 0):
    #     if comparisonNumber >= 1000:
    #         char = "M"
    #         textString += char
    #         comparisonNumber -= 1000
        
    #     elif comparisonNumber >= 900:
    #         char = "CM"
    #         textString += char
    #         comparisonNumber -= 900
        
    #     elif comparisonNumber >= 500:
    #         char = "D"
    #         textString += char
    #         comparisonNumber -= 500
        
    #     elif comparisonNumber >= 400:
    #         char = "CD"
    #         textString += char
    #         comparisonNumber -= 400
            
    #     elif comparisonNumber >= 100:
    #         char = "C"
    #         textString += char
    #         comparisonNumber -= 100
        
    #     elif comparisonNumber >= 90:
    #         char = "XC"
    #         textString += char
    #         comparisonNumber -= 90
            
    #     elif comparisonNumber >= 50:
    #         char = "L"
    #         textString += char
    #         comparisonNumber -= 50
            
    #     elif comparisonNumber >= 40:
    #         char = "XL"
    #         textString += char
    #         comparisonNumber -= 900
            
    #     elif comparisonNumber >= 10:
    #         char = "X"
    #         textString += char
    #         comparisonNumber -= 10
            
    #     elif comparisonNumber >= 9:
    #         char = "IX"
    #         textString += char
    #         comparisonNumber -= 9

    #     elif comparisonNumber >= 5:
    #         char = "V"
    #         textString += char
    #         comparisonNumber -= 5

    #     elif comparisonNumber >= 4:
    #         char = "IV"
    #         textString += char
    #         comparisonNumber -= 4
            
    #     elif comparisonNumber >= 1:
    #         char = "I"
    #         textString += char
    #         comparisonNumber -= 1
            
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

    romanNumeralsLabel.config(text = romanNumerals)
    stopwatchLabel.config(text = timeFormat)
    
    window.after(1000, updateDisplay)

window.config(background = "black")
backgroundFrame = Frame(window, background = "black")
stopwatchLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans MS", 40, "bold"), text = "00:00:00")
romanNumeralsLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans Ms", 40, "bold"))

runningTimer()
backgroundFrame.pack()
stopwatchLabel.pack()
romanNumeralsLabel.pack()

window.mainloop()
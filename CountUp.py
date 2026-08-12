from tkinter import *
import time, math

max_seconds = 10
elapsedTime = 0
startTime = 0

window = Tk()
window.title("Count-up Stopwatch")

def runningTimer():
    global startTime
    startTime = time.time() - elapsedTime
    updateDisplay()

def updateDisplay():
    global elapsedTime
    elapsedTime = time.time() - startTime
    hours = minutes = seconds = 0
    
    if int(elapsedTime) <= max_seconds:
        minutes, seconds = divmod(int(elapsedTime), 60)
        hours, minutes = divmod(int(minutes), 60)
        stopwatchLabel.config(text = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
    
    window.after(1000, updateDisplay)

backgroundFrame = Frame(window, background = "black")
stopwatchLabel = Label(backgroundFrame, background = "black", foreground = "white", font = ("Comic Sans MS", 40, "bold"), text = "00:00:00")

runningTimer()
backgroundFrame.pack()
stopwatchLabel.pack()

window.mainloop()
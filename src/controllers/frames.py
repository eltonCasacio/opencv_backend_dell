
import threading

outputVideolayer01 = None
outputVideolayer02 = None
outputVideolayer03 = None
outputVideolayer04 = None
outputVideolayer05 = None


def changeState_outputVideoLayer01(input):
    global outputVideolayer01
    outputVideolayer01 = input


def changeState_outputVideoLayer02(input):
    global outputVideolayer02
    outputVideolayer02 = input


def changeState_outputVideoLayer03(input):
    global outputVideolayer03
    outputVideolayer03 = input


def changeState_outputVideoLayer04(input):
    global outputVideolayer04
    outputVideolayer04 = input


def changeState_outputVideoLayer05(input):
    global outputVideolayer05
    outputVideolayer05 = input


lock = threading.Lock()

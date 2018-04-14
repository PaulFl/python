import numpy as np
import matplotlib.pyplot as plt


def map(value, inMin, inMax, outMin, outMax):
    coeff = (outMax - outMin)/(inMax - inMin)
    result = (value - inMin) * coeff + outMin
    return result
    
def plotBatteryPercentage():
    mapBatteryPercentage = [3.26, 3.435, 3.525, 3.635, 3.715, 3.79, 3.86, 3.94, 4.02, 4.07, 4.2]
    xAxis = [i*10 for i in range(11)]
    plt.plot(xAxis, mapBatteryPercentage)
    plt.show()

def batteryPercentage(voltage):
    mapBatteryPercentage = [3.26, 3.435, 3.525, 3.635, 3.715, 3.79, 3.86, 3.94, 4.02, 4.07, 4.2]
    batteryPercentage = 0
    battRange = 0
    for i in range(10):
        if (voltage >= mapBatteryPercentage[i]*10  and voltage <= mapBatteryPercentage[i+1]*10):
            battRange = i
    print("Batt range: " + str(battRange))
    batteryPercentage = int(map(voltage, mapBatteryPercentage[battRange] * 10, mapBatteryPercentage[battRange + 1] * 10, battRange * 10, (battRange + 1) * 10))  #Linear approximation beetween two values of mapBatteryPercentage
    if (voltage <= mapBatteryPercentage[0] * 10):
         batteryPercentage = 0
    elif (voltage >= mapBatteryPercentage[10] * 10):
         batteryPercentage = 100
    return batteryPercentage
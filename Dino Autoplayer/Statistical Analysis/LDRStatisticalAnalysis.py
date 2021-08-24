import time
import math
import board
import busio
import StandardDeviationCalculator
import adafruit_ads1x15.ads1015 as ADS                      #Importing the ADC module
from adafruit_ads1x15.analog_in import AnalogIn



def Main():
    if __name__ == "__main__":
        i2c = busio.I2C(board.SCL, board.SDA)                       #Initialising the I2C Bus
        ads = ADS.ADS1015(i2c)                                      #sets the ads object to the 1015, and using i2c communication
        chan0 = AnalogIn(ads, ADS.P0)                               #instantiates channel 0 to an analogue input, using the ads object
        length = 101                                                #sets the length of all lists
    
        totalVoltage = 0
        totalValue = 0
        voltages = [None] * length                                  #pre setting the length of the list to ensure it does not change upon each iteration
        values = [None] * length
    
        for c in range(length):
            print("LDR: Value: {:>5}\t Voltage: {:>5.3f}".format(chan0.value, chan0.voltage))
            time.sleep(0.05)                                                                  #sampling at 20Hz
            voltages[c] = chan0.voltage                                                       #sets the index of c to the voltages and values
            values[c] = chan0.value

        #Needs to calculate the population standard deviation of the voltages and values:

        print("Values: ", StandardDeviationCalculator.findStandardDeviation(values))           #calls and prints the result of the standard deviation calculator function
        print("Voltages: ", StandardDeviationCalculator.findStandardDeviation(voltages))



Main()

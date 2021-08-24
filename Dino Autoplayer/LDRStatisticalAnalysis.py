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
        ads = ADS.ADS1015(i2c)
        chan0 = AnalogIn(ads, ADS.P0)
        length = 101
    
        totalVoltage = 0
        totalValue = 0
        voltages = [None] * length
        values = [None] * length
    
        for c in range(length):
            print("LDR: Value: {:>5}\t Voltage: {:>5.3f}".format(chan0.value, chan0.voltage))
            time.sleep(0.05)
            voltages[c] = chan0.voltage
            values[c] = chan0.value

    #Needs to calculate the population standard deviation of the voltages and values:

        print("Values: ", StandardDeviationCalculator.findStandardDeviation(values))
        print("Voltages: ", StandardDeviationCalculator.findStandardDeviation(voltages))



Main()

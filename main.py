import serial
import serial.tools.list_ports
import glob
import sys
import time

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            if "USB" in port:# this part is for linux
                result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':

    sensorList = []
    ports = serial_ports()
    for port in ports:
        try:
            sensorList.append(serial.Serial(port))
        except:
            pass
    for sensor in sensorList:# print data from all sensors
        byte = sensor.readline()
        print(byte.decode())
    

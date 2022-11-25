import serial
import serial.tools.list_ports
import glob
import sys

ser = serial.Serial()


def open(port):
    ser.port = port
    try:
        ser.open() 
    except:
        open()
def close():
    ser.close()


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
            if "USB" in port:
            	result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
   
    
    ports = serial_ports()
    print(ports)
    
    open(ports[0])

    while True:
        byte = ser.readline()
        print(byte.decode())
    
    
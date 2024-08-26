import serial

read = [0]

try:
    ser = serial.Serial(port="COM4", baudrate=9600, bytesize=8, parity=serial.PARITY_EVEN, stopbits=2, timeout=6, write_timeout=5)
    ret = ser.write(read)
    print(ret)
    rd = ser.read(1024).decode("utf-8")
    print(rd)
except Exception as e:
    print(e)
finally:
    ser.close()
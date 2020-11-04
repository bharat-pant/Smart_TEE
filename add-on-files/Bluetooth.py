import bluetooth
import RPi.GPIO as GPIO  # calling for header file which helps in using GPIOs of PI

LED_1 = 21
LED_2 = 22
LED_3 = 23
LED_4 = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)
GPIO.setup(LED_4, GPIO.OUT)
GPIO.cleanup()
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_socket.bind(("", port))
server_socket.listen(1)

try:
    client_socket, address = server_socket.accept()
    print("Accepted connection from ", address)
    while True:

        data = client_socket.recv(1024)
        print("Received: %s" % data)
        if data == "1":  # if '1' is sent from the Android App, turn OFF the LED
            print("GPIO 21 LOW, LED OFF")
            GPIO.output(LED_1, 1)
        elif data == "2":  # if '2' is sent from the Android App, turn OFF the LED
            print("GPIO 21 HIGH, LED ON")
            GPIO.output(LED_2, 1)
        elif data == "3":  # if '3' is sent from the Android App, turn OFF the LED
            print("GPIO 21 LOW, LED OFF")
            GPIO.output(LED_3, 1)
        elif data == "4":  # if '4' is sent from the Android App, turn OFF the LED
            print("GPIO 21 LOW, LED OFF")
            GPIO.output(LED_4, 1)
        else:
            break
        client_socket.close()
        server_socket.close()

except:
    pass



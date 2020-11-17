import cv2, multiprocessing, time, math, bluetooth
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
number_of_cars = []
order_of_ambulance = [0]
threshold = 16
initial_timer_1, initial_timer_2, initial_timer_3, initial_timer_4=40, 40, 40, 40
car_cascade = cv2.CascadeClassifier('/home/pi/Desktop/cars.xml')     # CARS CLASSIFIER
count, n = 0, 0

""" LANE CHECK 1 VERIFIED FOR ALL ERRORS"""
def lane_check_1(q1, fg1, order):
    global cars_lane_1, set_lane_1
    set_lane_1 = set()
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    time.sleep(0.1)
    t_end = time.time() + 5
    queue_value = 0

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_1 = len(cars)
        set_lane_1.add(cars_lane_1)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord("q") or max(set_lane_1) > threshold:
            queue_value = 1
            order.put(1)
            break
        elif time.time() >= t_end:
            time.sleep(1)
            # order.put(0)
            break

    q1.put(max(set_lane_1))
    fg1.put(queue_value)
    time.sleep(1)
    cv2.destroyAllWindows()
########################################################################################################################


""" LANE CHECK 2 VERIFIED FOR ALL ERROR """


def lane_check_2(q2, fg2, order):
    set_lane_2 = set()
    cap = cv2.VideoCapture('/home/pi/Downloads/jan28.avi')
    t_end = time.time()+10
    queue_value = 0
    while True:
        ret, frames = cap.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.2, 1)
        cars_lane_2 = len(cars)
        set_lane_2.add(cars_lane_2)
        if cv2.waitKey(33) == 27 or max(set_lane_2) > threshold:
            queue_value = 1
            order.put(2)
            time.sleep(1)
            break
        elif time.time() >= t_end:
            # order.put(0)
            break
    q2.put(max(set_lane_2))
    fg2.put(queue_value)
    time.sleep(1)
    cv2.destroyAllWindows()
########################################################################################################################


"""LANE CHECK 3 VERIFIED FOR ALL ERRORS"""


def lane_check_3(q3, fg3, order):
    set_lane_3 = set()
    cap = cv2.VideoCapture('/home/pi/Downloads/march9.avi')
    t_end = time.time() + 10
    queue_value = 0
    while True:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.2, 1)
        cars_lane_3 = len(cars)
        set_lane_3.add(cars_lane_3)
        if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold:                       # Wait for Esc key to stop
            queue_value = 1
            order.put(3)
            time.sleep(1)
            break
        elif time.time() >= t_end:
            # order.put(0)
            break
    q3.put(max(set_lane_3))
    time.sleep(1)
    fg3.put(queue_value)
    time.sleep(1)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
########################################################################################################################


""" LANE CHECK 4 VERIFIED FOR ALL ERRORS """


def lane_check_4(q4, fg4, order):
    set_lane_4 = set()
    cap = cv2.VideoCapture('/home/pi/Downloads/april21.avi')
    t_end = time.time() + 10
    queue_value = 0
    while True:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_4 = len(cars)
        set_lane_4.add(cars_lane_4)
        if cv2.waitKey(33) == 27 or max(set_lane_4)>threshold:      # Wait for Esc key to stop
            queue_value = 1
            time.sleep(1)
            order.put(4)
            break
        elif time.time() >= t_end:
            #order.put(0)
            break
    q4.put(max(set_lane_4))
    fg4.put(queue_value)
    time.sleep(1)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
########################################################################################################################


def algorithm(a1, a2, a3, a4):                          # FUNCTION FOR ALGORITHM
    global initial_timer_1, initial_timer_2, initial_timer_3, initial_timer_4
    value_1 = a1 / (a1 + a2 + a3 + a4)
    value_2 = a2 / (a1 + a2 + a3 + a4)
    value_3 = a3 / (a1 + a2 + a3 + a4)
    value_4 = a4 / (a1 + a2 + a3 + a4)
    update_1 = initial_timer_1 + initial_timer_1 * value_1 * (math.log(value_1 / 0.25, 10))
    update_2 = initial_timer_2 + initial_timer_2 * value_2 * (math.log(value_2 / 0.25, 10))
    update_3 = initial_timer_3 + initial_timer_3 * value_3 * (math.log(value_3 / 0.25, 10))
    update_4 = initial_timer_4 + initial_timer_4 * value_4 * (math.log(value_4 / 0.25, 10))
    initial_timer_1 = update_1
    initial_timer_2 = update_2
    initial_timer_3 = update_3
    initial_timer_4 = update_4
    return initial_timer_1, initial_timer_2, initial_timer_3, initial_timer_4


def bluetooth_call():
    global n
    try:
        client.setblocking(0)
        data = client.recv(1024)
        # d = data.decode('utf-8')
        ab = str(data.decode('utf-8'))
        if int(ab) == 0:
            order_of_ambulance.pop(0)
            return 0
        else:
            order_of_ambulance.append(int(ab))
            print(type(ab))
            return order_of_ambulance

    except:
        print("No ambulance call")
        return "9"
        # if a=="1" or a==4"" or a=="2" or a=="3":


def ambulance_call(a):
    global n
    while len(a) != 0:
        if a[0] == "1":
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(11, GPIO.OUT)
            GPIO.setup(22, GPIO.OUT)
            GPIO.setup(32, GPIO.OUT)
            GPIO.setup(36, GPIO.OUT)
            while True:

                GPIO.output(11, True)
                GPIO.output(22, True)
                GPIO.output(32, True)
                GPIO.output(36, True)
                time.sleep(1)
                b = bluetooth_call()
                if b == "0":
                    GPIO.cleanup()
                    break
                else:
                    a = b
                    # return 0

        elif a[0] == "2":

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(13, GPIO.OUT)
            GPIO.setup(18, GPIO.OUT)
            GPIO.setup(32, GPIO.OUT)
            GPIO.setup(36, GPIO.OUT)
            while True:
                GPIO.output(13, True)
                GPIO.output(18, True)
                GPIO.output(32, True)
                GPIO.output(36, True)
                time.sleep(1)
                b = bluetooth_call()
                if b == "0":
                    GPIO.cleanup()
                    break
                else:
                    a = b
                    # return 0

        elif a[0] == "3":
            GPIO.setmode(GPIO.BOARD)

            GPIO.setup(15, GPIO.OUT)
            GPIO.setup(22, GPIO.OUT)
            GPIO.setup(18, GPIO.OUT)
            GPIO.setup(36, GPIO.OUT)
            while True:
                GPIO.output(15, True)
                GPIO.output(18, True)
                GPIO.output(22, True)
                GPIO.output(36, True)
                time.sleep(1)
                b = bluetooth_call()
                if b == "0":
                    GPIO.cleanup()
                    break
                else:
                    a = b
                    # return 0

        elif a[0] == "4":
            GPIO.setmode(GPIO.BOARD)

            GPIO.setup(16, GPIO.OUT)
            GPIO.setup(22, GPIO.OUT)
            GPIO.setup(32, GPIO.OUT)
            GPIO.setup(18, GPIO.OUT)
            while True:
                GPIO.output(16, True)
                GPIO.output(18, True)
                GPIO.output(22, True)
                GPIO.output(32, True)
                time.sleep(1)
                b = bluetooth_call()
                if b == "0":
                    GPIO.cleanup()
                    # return 0
                    break
                else:
                    a = b
                    # return 0
        a.pop(0)


def normal_timer():
    
    global count
    count = count + 1
    if count >= 40:
        count = 0
    if count % 4 == 1:
        print("lane1 green baaki saare red")
        normal_time_lane_1 = time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        print(count)
        #LED = 11
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        while time.time() < normal_time_lane_1:
            
            GPIO.output(11, True)
            GPIO.output(22, True)
            GPIO.output(32, True)
            GPIO.output(36, True)
            time.sleep(1)
            a = bluetooth_call()
            if len(a) != 0:
                print("Ambulance call")
                GPIO.cleanup()
                ambulance_call(a)
                break
                #break

        GPIO.cleanup()

    elif count % 4 == 2:
        print("lane2 green baaki saare red")
        normal_time_lane_2 = time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        #LED = 13
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        
        while time.time() < normal_time_lane_2:
            
            GPIO.output(13, True)
            GPIO.output(18, True)
            GPIO.output(32, True)
            GPIO.output(36, True)
            time.sleep(1)
            a = bluetooth_call()
            if len(a) != 0:
                print("Ambulance call")
                GPIO.cleanup()
                ambulance_call(a)
                break
                #break
            
                
        GPIO.cleanup()

    elif count % 4 == 3:
        print("lane3 green baaki saare red")
        normal_time_lane_3 = time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        #LED = 15
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        while time.time() < normal_time_lane_3:
            GPIO.output(15, True)
            GPIO.output(18, True)
            GPIO.output(22, True)
            GPIO.output(36, True)
            time.sleep(1)
            a = bluetooth_call()
            if len(a) != 0:
                print("Ambulance call")
                GPIO.cleanup()
                ambulance_call(a)
                break
                #break

        GPIO.cleanup()

    else:
        print("lane 4 green baaki saare red")
        normal_time_lane_4= time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        #LED = 16
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        while time.time() < normal_time_lane_4:
            
            GPIO.output(16, True)
            GPIO.output(18, True)
            GPIO.output(22, True)
            GPIO.output(32, True)
            time.sleep(1)
            a=bluetooth_call()
            if len(a) != 0:
                print("Ambulance call")
                GPIO.cleanup()
                ambulance_call(a)
                break

        GPIO.cleanup()


if __name__ == '__main__':
    host = ""
    port = 1
    server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print('Bluetooth Socket Created')
    try:
        server.bind((host, port))
        print("Bluetooth Binding Completed")
    except:
        print("Bluetooth Binding Failed")
    try:
        server.listen(1)
        client, address = server.accept()
        print("Connected To", address)
        print("Client:", client)
        
    except:
        print("No response")
        client.close()
        server.close()
        pass
    with multiprocessing.Manager() as manager:
        value = manager.list()
        q1 = multiprocessing.Queue()
        q2 = multiprocessing.Queue()
        q3 = multiprocessing.Queue()
        q4 = multiprocessing.Queue()
        fg1 = multiprocessing.Queue()
        fg2 = multiprocessing.Queue()
        fg3 = multiprocessing.Queue()
        fg4 = multiprocessing.Queue()
        fg5 = multiprocessing.Queue()
        order = multiprocessing.Queue()

        while True:
            process1 = multiprocessing.Process(target=lane_check_1,args=(q1,fg1,order,))
            process2 = multiprocessing.Process(target=lane_check_2,args=(q2,fg2,order,))
            process3 = multiprocessing.Process(target=lane_check_3,args=(q3,fg3,order,))
            process4 = multiprocessing.Process(target=lane_check_4,args=(q4,fg4,order,))
            process1.start(),process2.start(), process3.start(), process4.start()
            
            time.sleep(2)
            try:
                flag1 = fg1.get()
            except:
                flag1 = 0
            try:
                flag2 = fg2.get()
            except:
                flag2=0
            try:    
                flag3 = fg3.get()
            except:
                flag3=0
            try:
                flag4 = fg4.get()
            except:
                flag4=0
            

            a1, a2, a3, a4 = q1.get(), q2.get(), q3.get(), q4.get()

            print(flag1, flag2, flag3, flag4)
            process1.terminate()
            process2.terminate()
            process3.terminate()
            process4.terminate()

            if a1 == 0:
                a1 = 1
            elif a2 == 0:
                a2 = 1
            elif a3 == 0:
                a3 = 0
            elif a4 == 0:
                a4 = 1
            else:
                pass

            number_of_cars.append(a1)
            number_of_cars.append(a2)
            number_of_cars.append(a3)
            number_of_cars.append(a4)
            print(number_of_cars)
            time1,time2,time3,time4=algorithm(a1,a2,a3,a4)

            print(algorithm(a1,a2,a3,a4))
            a=9
            for i in range(order.qsize()):
                z = order.get()
                print("value is ", z)
                if z == 1:
                    time_1 = time.time() + time1 
                    GPIO.setmode(GPIO.BOARD)
                    #LED = 11
                    GPIO.setup(11, GPIO.OUT)
                    GPIO.setup(22, GPIO.OUT)
                    GPIO.setup(32, GPIO.OUT)
                    GPIO.setup(36, GPIO.OUT)
                    while time.time() < time_1:
                        
                        GPIO.output(11, True)
                        GPIO.output(22, True)
                        GPIO.output(32, True)
                        GPIO.output(36, True)
                        time.sleep(1)
                        a = bluetooth_call()
                        if a=="1" or a=="2" or a=="3" or a=="4":
                            print("Ambulance call")
                            GPIO.cleanup()
                            ambulance_call(a)
                            break        
                    #GPIO.cleanup()
                    print("green on lane 1")
                    print("red on other lanes")

                elif z == 2:
                    time_2 = time.time() + time2
                    GPIO.setmode(GPIO.BOARD)
                    #LED = 13
                    GPIO.setup(13, GPIO.OUT)
                    GPIO.setup(18, GPIO.OUT)
                    GPIO.setup(32, GPIO.OUT)
                    GPIO.setup(36, GPIO.OUT)
                    while time.time() < time_2:
                        
                        GPIO.output(13, True)
                        GPIO.output(18, True)
                        GPIO.output(32, True)
                        GPIO.output(36, True)
                        time.sleep(1)
                        a=bluetooth_call()
                        if a=="1" or a=="2" or a=="3" or a=="4":
                            print("Ambulance call")
                            GPIO.cleanup()
                            ambulance_call(a)
                            break
                    
                            
                    #GPIO.cleanup()
                    
                    # print("green on lane 2")
                    # print("red on other lanes")

                elif z == 3:
                    time_3 = time.time() + time3
                    GPIO.setmode(GPIO.BOARD)
                    #LED = 15
                    GPIO.setup(15, GPIO.OUT)
                    GPIO.setup(22, GPIO.OUT)
                    GPIO.setup(18, GPIO.OUT)
                    GPIO.setup(36, GPIO.OUT)
                    while time.time() < time_3:
                        
                        GPIO.output(15, True)
                        GPIO.output(18, True)
                        GPIO.output(22, True)
                        GPIO.output(36, True)
                        time.sleep(1)
                        a=bluetooth_call()
                        if a=="1" or a=="2" or a=="3" or a=="4":
                            print("Ambulance call")
                            GPIO.cleanup()
                            ambulance_call(a)
                            break
                        
                            
                    #GPIO.cleanup()
                    # print("green on lane 3")
                    # print("red on other lanes")

                elif z == 4:
                    time_4 = time.time() + time4
                    GPIO.setmode(GPIO.BOARD)
                    #LED = 16
                    GPIO.setup(16, GPIO.OUT)
                    GPIO.setup(22, GPIO.OUT)
                    GPIO.setup(18, GPIO.OUT)
                    GPIO.setup(32, GPIO.OUT)
                    while time.time() < time_4:
                        
                        GPIO.output(16,True)
                        GPIO.output(18, True)
                        GPIO.output(22, True)
                        GPIO.output(32, True)
                        time.sleep(1)
                        a=bluetooth_call()
                        if a=="1" or a=="2" or a=="3" or a=="4":
                            print("Ambulance call")
                            GPIO.cleanup()
                            ambulance_call(a)
                            break
                        
                            
                    #GPIO.cleanup()
                    # print("green on lane 4")
                    # print("red on other lanes")
            else:
                normal_timer()
                print("function call back to processing")

"""YAAD RAKHNA KI 4 FUNCTIONS BANANE HAI AND HAR FUNCTION ME RESPECTIVE GREEN KARKE BAAKI SAARE RED KARNE HAI"""


""" YAAD RAKHNA HAI KI BLUETOOTH WALA MAIN FUNCTION ME PROCESS DECLARATION KE BAAD AAYEGA AND BLUETOOTH WALE ME GPIO 
ASSIGN KARNI HAI """


""" DATE: 17TH NOVEMBER UPDATE """
""" MULTIPLE EV CORRECTED"""
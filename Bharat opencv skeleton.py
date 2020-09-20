import cv2,multiprocessing,time,math
cars_lane_1, cars_lane_2,cars_lane_3,cars_lane_4,set_lane_1,set_lane_2,set_lane_3,set_lane_4,flag1,flag2,flag3,flag4 = 0,0,0,0,0,0,0,0,0,0,0,0
lane_order=[]
threshold=10
car_cascade = cv2.CascadeClassifier('cars121004.xml')           # Trained XML classifiers describes some features of some object we want to detect
initial_timer=40

def lane_check_1(q1,fg1,order):
    global cars_lane_1,set_lane_1
    set_lane_1=set()
    cap = cv2.VideoCapture(0)
    t_end=time.time()+10
    queue_value=0

    while time.time()<t_end:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_1=len(cars)
        set_lane_1.add(cars_lane_1)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_1)>threshold:                              #threshold ki jagah 10 dala hai
            queue_value=1
            order.put(1)
            break
    q1.put(max(set_lane_1))
    fg1.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


def lane_check_2(q2,fg2,order):
    global cars_lane_2, set_lane_2
    set_lane_2=set()
    cap = cv2.VideoCapture('videos/jan28.avi')
    t_end=time.time()+10
    queue_value=0
    while time.time()<t_end:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_2=len(cars)
        set_lane_2.add(cars_lane_2)

        for (x, y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_2)>threshold:                                # Wait for Esc key to stop
            queue_value=1
            order.put(2)
            break
    q2.put(max(set_lane_2))
    fg2.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usag


def lane_check_3(q3,fg3,order):
    global cars_lane_3, set_lane_3
    set_lane_3=set()
    cap = cv2.VideoCapture('videos/march9.avi')
    t_end = time.time() + 10
    queue_value=0
    while time.time() < t_end:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_3=len(cars)
        set_lane_3.add(cars_lane_3)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold:                       # Wait for Esc key to stop
            queue_value=1
            order.put(3)
            break
    q3.put(max(set_lane_3))
    fg3.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


def lane_check_4(q4,fg4,order):
    global cars_lane_4,set_lane_4
    set_lane_4=set()
    cap = cv2.VideoCapture('videos/april21.avi')
    t_end = time.time() + 10
    queue_value=0
    while time.time() < t_end:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_4=len(cars)
        set_lane_4.add(cars_lane_4)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_4)>threshold:      # Wait for Esc key to stop
            queue_value=1
            order.put(4)
            break
    q4.put(max(set_lane_4))
    fg4.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


def light_lane_1():
    initial_timer=40
    initial_timer_1= time.time()+initial_timer
    while time.time()<initial_timer_1:
        print("GREEN")
        time.sleep(1)


def light_lane_2():
    initial_timer = 15
    initial_timer_2 = time.time() + initial_timer
    while time.time() < initial_timer_2:
        print("GREEN_1")
        time.sleep(2)


def light_lane_3():
    initial_timer = 40
    initial_timer_3 = time.time() + initial_timer
    while time.time() < initial_timer_3:
        print("GREEN")
        time.sleep(1)


def light_lane_4():
    initial_timer = 10
    initial_timer_4 = time.time() + initial_timer
    while time.time() < initial_timer_4:
        print("GREEN_2")
        time.sleep(1)


def red_light():
    initial_timer = 40
    initial_timer_red = time.time() + initial_timer
    while time.time() < initial_timer_red:
        print("RED")
        time.sleep(1)


if __name__ == '__main__':
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
        order = multiprocessing.Queue()

        while True:
            process5 = multiprocessing.Process(target=light_lane_1, args=())
            process6 = multiprocessing.Process(target=light_lane_2, args=())
            process7 = multiprocessing.Process(target=light_lane_3, args=())
            process8 = multiprocessing.Process(target=light_lane_4, args=())
            process1=multiprocessing.Process(target=lane_check_1,args=(q1,fg1,order,))
            process2=multiprocessing.Process(target=lane_check_2,args=(q2,fg2,order,))
            process3=multiprocessing.Process(target=lane_check_3,args=(q3,fg3,order,))
            process4=multiprocessing.Process(target=lane_check_4,args=(q4,fg4,order,))
            process1.start(),process2.start(), process3.start(), process4.start()#,process5.start(),process6.start(), process7.start(), process8.start()
            flag1 = fg1.get()
            flag2 = fg2.get()
            flag3 = fg3.get()
            flag4 = fg4.get()

            a1,a2,a3,a4=q1.get(),q2.get(),q3.get(),q4.get()

            print(flag1,flag2,flag3,flag4)

            if flag1==1 or flag2==1 or flag3==1 or flag4==1:
                # process5.terminate()
                # process6.terminate()
                # process7.terminate()
                # process8.terminate()
                process1.terminate()
                process2.terminate()
                process3.terminate()
                process4.terminate()
                lane_order.append(a1)
                lane_order.append(a2)
                lane_order.append(a3)
                lane_order.append(a4)

            if a1==0:
                a1=1
            elif a2==0:
                a2=1
            elif a3==0:
                a3=0
            elif a4==0:
                a4=1
            else:
                pass


###########################################################################################################

            """VALUE UPDATES"""

            value_1=a1/ (a1+a2+a3+a4)
            value_2 = a2 / (a1 + a2 + a3 + a4)
            value_3 = a3 / (a1 + a2 + a3 + a4)
            value_4 = a4 / (a1 + a2 + a3 + a4)
            update_1 = initial_timer + initial_timer * value_1 * (math.log(value_1/0.25 , 10))
            update_2 = initial_timer + initial_timer * value_2 * (math.log(value_2/0.25 , 10))
            update_3 = initial_timer + initial_timer * value_3 * (math.log(value_3/0.25 , 10))
            update_4 = initial_timer + initial_timer * value_4 * (math.log(value_4/0.25 , 10))

###########################################################################################################


            print(update_1,update_2,update_3,update_4)
            for i in iter(order.get,'STOP'):
                if i == 1:
                    print("LANE 1 GIVEN GREEN")
                    print("OTHER LANES GIVEN RED")
                elif i == 2:
                    print("LANE 2 GIVEN GREEN")
                    print("OTHER LANES GIVEN RED")
                    process6.start()
                    process6.join()
                elif i == 3:
                    print("LANE 3 GIVEN GREEN")
                    print("OTHER LANES GIVEN RED")
                elif i == 4:
                    print("LANE 4 GIVEN GREEN")
                    print("OTHER LANES GIVEN RED")
                    process8.start()
                else:
                    print("NORMAL TIMER")
                time.sleep(2)
                print(lane_order)
                print(lane_order.index(max(lane_order)))

'''flag updation to be performed'''

# LANE DETECTION PARTIALLY PERFORMED INSTEAD OF FLAG PUSH IN QUEUE AND GET BACK VALUES

# LANE DETECTION DONE LANE TIMER PARTIALLY PERFORMED
# VALUE UPDATE LEFT

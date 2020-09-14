import cv2
import multiprocessing
cars_lane_1, cars_lane_2,cars_lane_3,cars_lane_4,set_lane_1,set_lane_2,set_lane_3,set_lane_4 = 0,0,0,0,4,4,4,4
lane_order=[]
flag1,flag2,flag3,flag4=0,0,0,0
threshold=15
car_cascade = cv2.CascadeClassifier('cars121004.xml')           # Trained XML classifiers describes some features of some object we want to detect


class Harsh:
    global cars_lane_1
    global set_lane_1
    global cars_lane_2
    global set_lane_2
    global cars_lane_3
    global set_lane_3
    global cars_lane_4
    global set_lane_4

    def lane_check_1(self,q1,fg1):
        global cars_lane_1
        global set_lane_1
        global cars_lane_2
        global set_lane_2
        global cars_lane_3
        global set_lane_3
        global cars_lane_4
        global set_lane_4
        set_lane_1=set()
        cap = cv2.VideoCapture(0)

        while True:
            ret, frames = cap.read()                                    # reads frames from a video
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            cars_lane_1=len(cars)
            set_lane_1.add(cars_lane_1)
            q1.put(max(set_lane_1))
        ######################################################################### last commit made a list to store max value
            for (x,y,w,h) in cars:
                cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

            cv2.imshow('video2', frames)                                # Display frames in a window
            if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold: #threshold ki jagah 10 dala hai
                break
        fg1.put(1)
        cv2.destroyAllWindows()                                         # De-allocate any associated memory usage

    def lane_check_2(self,q2,fg2):
        global cars_lane_1
        global set_lane_1
        global cars_lane_2
        global set_lane_2
        global cars_lane_3
        global set_lane_3
        global cars_lane_4
        global set_lane_4
        set_lane_2=set()
        cap = cv2.VideoCapture('videos/jan28.avi')

        while True:
            ret, frames = cap.read()                                    # reads frames from a video
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            cars_lane_2=len(cars)
            set_lane_2.add(cars_lane_2)
            q2.put(max(set_lane_2))
        ###############################################################commit change 2
            for (x,y,w,h) in cars:
                cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.imshow('video2', frames)                                # Display frames in a window
            if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold:   #threshold ki jagah 10 dala hai                                   # Wait for Esc key to stop
                break
        fg2.put(1)
        cv2.destroyAllWindows()                                         # De-allocate any associated memory usag

    def lane_check_3(self,q3,fg3):
        global cars_lane_1
        global set_lane_1
        global cars_lane_2
        global set_lane_2
        global cars_lane_3
        global set_lane_3
        global cars_lane_4
        global set_lane_4
        set_lane_3=set()
        cap = cv2.VideoCapture('videos/march9.avi')

        while True:
            ret, frames = cap.read()                                    # reads frames from a video
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            cars_lane_3=len(cars)
            set_lane_3.add(cars_lane_3)
            print(max(set_lane_3))
            q3.put(max(set_lane_3))


            for (x,y,w,h) in cars:
                cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

            cv2.imshow('video2', frames)                                # Display frames in a window
            if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold:            #threshold ki jagah 10 dala hai                       # Wait for Esc key to stop
                break
        fg3.put(1)
        cv2.destroyAllWindows()                                         # De-allocate any associated memory usage

    def lane_check_4(self,q4,fg4):
        global cars_lane_1
        global set_lane_1
        global cars_lane_2
        global set_lane_2
        global cars_lane_3
        global set_lane_3
        global cars_lane_4
        global set_lane_4
        set_lane_4=set()
        cap = cv2.VideoCapture('videos/april21.avi')

        while True:
            ret, frames = cap.read()                                    # reads frames from a video
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            cars_lane_4=len(cars)
            set_lane_4.add(cars_lane_4)
            q4.put(max(set_lane_4))
            print(max(set_lane_4))

            for (x,y,w,h) in cars:
                cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

            cv2.imshow('video2', frames)                                # Display frames in a window
            if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold:            #threshold ki jagah 10 dala hai                       # Wait for Esc key to stop
                break
        fg4.put(1)
        cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


if __name__ == '__main__':
    h=Harsh()
    q1=multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    q3 = multiprocessing.Queue()
    q4 = multiprocessing.Queue()
    fg1 = multiprocessing.Queue()
    fg2 = multiprocessing.Queue()
    fg3 = multiprocessing.Queue()
    fg4 = multiprocessing.Queue()

    process1=multiprocessing.Process(target=h.lane_check_1,args=(q1,fg1,))
    process2=multiprocessing.Process(target=h.lane_check_2,args=(q2,fg2,))
    process3=multiprocessing.Process(target=h.lane_check_3,args=(q3,fg3,))
    process4=multiprocessing.Process(target=h.lane_check_4,args=(q4,fg4,))
    process1.start(),process2.start(), process3.start(), process4.start()
    flag1 = fg1.get()
    flag2 = fg2.get()
    flag3 = fg3.get()
    flag4 = fg4.get()

    if flag1==1 or flag2==1 or flag3==1 or flag4==1:

        process1.terminate()
        process2.terminate()
        process3.terminate()
        process4.terminate()
        print("hello")
        print(q4.get())
        lane_order.append(q1.get())
        lane_order.append(q2.get())
        lane_order.append(q3.get())
        lane_order.append(q4.get())

'''flag updation to be performed'''


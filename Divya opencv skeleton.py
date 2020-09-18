import cv2
import time
from multiprocessing import Process

def func1():
    global lane_1
    lane_1 = list()
    cap = cv2.VideoCapture(r'Car.mp4')
    car_cascade = cv2.CascadeClassifier(r'cars121004.xml')
    for i in range(3):
        ret, frames = cap.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        time.sleep(5)
        a1 = len(cars)
        lane_1.append(a1)
        print('a1 is ', a1)
        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 0)
        cv2.imshow('video2', frames)
        if cv2.waitKey(33) == 27:
            break


def func2():
    global lane_2
    lane_2 = list()
    cap = cv2.VideoCapture(r'Car.mp4')
    car_cascade = cv2.CascadeClassifier(r'cars121004.xml')
    for i in range(3):
        ret, frames = cap.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        time.sleep(6)
        a2 = len(cars)
        lane_2.append(a2)
        print('a2 is ', a2)
        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video2', frames)
        if cv2.waitKey(33) == 27:
            break


def func3():
    global lane_3
    lane_3 = list()
    cap = cv2.VideoCapture(r'1038686156-preview.mp4')
    car_cascade = cv2.CascadeClassifier(r'cars121004.xml')
    for i in range(3):
        ret, frames = cap.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        time.sleep(7)
        a3 = len(cars)
        lane_3.append(a3)
        print('a3 is ', a3)
        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video2', frames)
        if cv2.waitKey(33) == 27:
            break


def func4():
    global lane_4
    lane_4 = list()
    cap = cv2.VideoCapture(r'Car_4.mp4')
    car_cascade = cv2.CascadeClassifier(r'cars121004.xml')
    for i in range(3):
        ret, frames = cap.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        time.sleep(8)
        a4 = len(cars)
        lane_4.append(a4)
        print('a4 is ', a4)
        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video2', frames)
        if cv2.waitKey(33) == 27:
            break

if __name__ == '__main__':

    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p3 = Process(target=func3)
    p3.start()
    p4 = Process(target=func4)
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()



cv2.destroyAllWindows()

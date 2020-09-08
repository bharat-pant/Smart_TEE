import cv2
import multiprocessing
count=0
count_object=set()
#cap = cv2.VideoCapture('1038686156-preview.mp4')                                       # capture frames from a video
cap = cv2.VideoCapture(0)                                       # capture frames from a video
car_cascade = cv2.CascadeClassifier('cars121004.xml')           # Trained XML classifiers describes some features of some object we want to detect

def lane_check_1():
    lane_number=1

    while True:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        c=len(cars)
        count_object.add(c)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27:                                   # Wait for Esc key to stop
            break
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
    print("MAXIMUM CARS DETECTED IS " + str(max(count_object)))
    print("number of cars in this lane is ", str(max(count_object)) )
    print(count_object)

if __name__ == '__main__':
    process1=multiprocessing.Process(target=lane_check_1)
    process1.start()
    process2=multiprocessing.Process(target=lane_check_1)
    process2.start()
    process3=multiprocessing.Process(target=lane_check_1)
    process3.start()

    process1.join()
    process2.join()
    process3.join()

cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


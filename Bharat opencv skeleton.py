import cv2
count=0
count_object=set()
cap = cv2.VideoCapture(0)                                       # capture frames from a video
car_cascade = cv2.CascadeClassifier('cars121004.xml')           # Trained XML classifiers describes some features of some object we want to detect
  
while True:
    ret, frames = cap.read()                                    # reads frames from a video
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    c=len(cars)
    print(c)

    for (x,y,w,h) in cars:
        count=count+1
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        count_object.add(count)
    else:
        count_object.add(0)
        count = 0

    cv2.imshow('video2', frames)                                # Display frames in a window
    if cv2.waitKey(33) == 27:                                   # Wait for Esc key to stop
        break
cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
print(count_object)
print("MAXIMUM CARS DETECTED IS " + str(max(count_object)))



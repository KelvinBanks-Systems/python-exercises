import cv2 as cv

# Capture video file for script
# Subtractor object
# Import mp4 Video by Joseph Eulo

video = cv.VideoCapture('2.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(300, 50)



# Visualize data via loop
while True:
    returnValue, frame = video.read()

    if returnValue:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

# Terminate Video/loop with button 'x'
        if cv.waitKey(5) == ord('X'):
            break
    else:
        video = cv.VideoCapture('2.mp4')


cv.destroyAllWindows()
video.release()
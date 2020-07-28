import cv2, time

video = cv2.VideoCapture(0)  # Capturing a video

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting a video to gray colors
    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(1)  # Adding some waiting time between frames (adjusting FPS)
    print(gray) 

    if key == ord("q"):  # To stop video press "q"
        break

video.release()
cv2.destroyAllWindows
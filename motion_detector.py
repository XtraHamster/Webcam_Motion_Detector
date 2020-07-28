import cv2, time

first_frame = None  # Define a first frame for next steps

video = cv2.VideoCapture(0)  # Capturing a video

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting a video to gray colors
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # Adding Gaussian blur --> better noise cancel, better conditions for motion detecting

    if first_frame is None:  # Assign first_frame to a variable, if already does not have
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)

    cv2.imshow("Grey Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)

    key = cv2.waitKey(1)  # Adding some waiting time between frames (adjusting FPS)
    print(gray) 

    if key == ord("q"):  # To stop video press "q"
        break

video.release()
cv2.destroyAllWindows
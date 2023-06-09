import cv2
import mediapipe as mp
import handtrackingmodule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
tracker = htm.handTracker()

while True:
        success,image = cap.read()
        image = tracker.handsFinder(image)
        lmList = tracker.positionFinder(image)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime -pTime)
        pTime = cTime

        cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Video",image)
        cv2.waitKey(1)
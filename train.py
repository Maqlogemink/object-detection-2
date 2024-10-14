import cv2

cap = cv2.VideoCapture(1)
fcc = cv2.CAP(*'XVID')
out = cv2.VideoWriter()
while (True) :
    ret, frame = cap.read()

    cv2.imshow('video capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


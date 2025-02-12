import cv2
import time
import mediapipe as mp

cap = cv2. VideoCapture (0)

mpHand = mp.solutions. hands
hands = mpHand. Hands () #ellerin tespiti ve konumlandırılması için
mpdraw = mp.solutions.drawing_utils #çizim

pTime = 0
cTime=0

while True:
    control, capture = cap.read()
    results = hands.process (capture)

    print (results.multi_hand_landmarks) #el tespiti kordinatları
    if results.multi_hand_landmarks: #her bir landmarks içerisinde gezilir.
        for handlms in results.multi_hand_landmarks: # handlms ile x,y ve z kordinatları alınır.
            mpdraw.draw_landmarks (capture, handlms, mpHand. HAND_CONNECTIONS)
            
            for number, lm in enumerate(handlms. landmark):
                print (number, lm) #number eklem numarası, lm-> x,y,z kordinatları
                h,w, c = capture.shape
                cx, cy= int(lm. x*w), int (lm.y*h)
                
                #işaret parmağının tespiti
                if ((number==5)| (number==6)| (number==7)| (number==8)): # bunu değiştirdikçe elin hangi eklemini alacağını söylemiş oluruz
                    cv2.circle(capture, (cx, cy), 20, (255,0,0), cv2. FILLED)
    #fps I
    cTime=time.time()
    fpd = 1/(cTime-pTime())
    pTime=cTime
    
    cv2.putText (capture, "FPS: "+str(int (fps)), (10,75), cv2. FONT_HERSHEY_PLAIN, 3, (255, 0, 0),5)

    cv2.imshow("capture", capture)
    
    if cv2.waitkey (1) & 0xFF == ord ("q"):
        break
cv2.destroyAllWindows()
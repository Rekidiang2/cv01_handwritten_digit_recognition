import cv2
import numpy as np

font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture()
#cop.set(cv2.CAP_PROP_FPS, 170)
# check if the webcam is open correctly
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Can not Open Webcam")
    
text = "Some text in a box"
(text_box_width, text_box_heigth) = cv2.getTextSize(text, font,
                                                    fontScale=font_scale, 
                                                    thickness=1)[0] 
text_offset_x = 10
text_offset_y = img.shape[0] - 25
#box padding
box_coords = ((text_offset_x, text_offset_y), 
              (text_offset_x + text_box_width  +2,
               text_offset_y - text_box_heigth -2))

cntr = 0;
while True:
    ret, frame = cap.read()
    cntr=cntr+1;
    if ((cntr%2)==0):
        gray = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (28,28), interpolation=cv2.INTER_AREA)
        newimg = tf.keras.utils.normalize(resized, axis=1)
        row_size = resized.shape[0]
        col_size = resized.shape[1]
        newimg = np.array(newimg).reshape(-1,row_size, col_size,1)
        preds = model.predict(newimg)
        status = np.argmax(preds)
        print(status)
        print(type(status))
        
        x1, y1, w1, h1 = 0,0,175, 75
        cv2.rectangle(frame, (x1,x1), (x1 + w1,y1+h1), (0,0,0), -1)
        cv2.putText(frame, status.astype(str), (x1 + int(w1/5), y1 + int(h1/2)), 
                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
        
        cv2.imshow('HandWritten Digit Recognition !!', frame)
        if cv2.waitKey(2)& 0xFF ==ord('q'):
                      break
cap.release()
cv2.destroyAllwindows()
    

import cv2 
from longest_word import get_words

word_obj = get_words()
word_list = word_obj.words
word_iter = iter(word_list)
output_text = next(word_iter)

font = cv2.FONT_HERSHEY_SIMPLEX
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
cap = cv2.VideoCapture(0) 
switch = False
thresh = False
thresh_val=0

while 1: 
    ret, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    cv2.putText(img,output_text,(200,200), font, 3, (255,0,0),2, cv2.LINE_AA)     
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        # Puts rectangle over eyes
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
        # Logic to check if user has broken the threshold value
        if(abs(thresh_val-y)>20 and thresh==True and switch == False):
            switch = True
            output_text = next(word_iter, "Out of words")
        elif(abs(thresh_val-y)<10 and switch==True and thresh==True):
            switch = False
    cv2.imshow('img',img) 
    k = cv2.waitKey(30) & 0xff
    if k == ord('q') or k==27: 
        break
    elif k == ord('m'):
        print('Reset')
        thresh_val = y
        thresh = True
cap.release() 
cv2.destroyAllWindows() 

#!/usr/bin/env python3

import argparse
import os
from pathlib import Path

import cv2

from longest_word import get_longest_words


def display_words(window_size: int, letters: str, **kwargs):
    word_list = get_longest_words(letters)
    word_iter = iter(word_list)
    output_text = next(word_iter)
    font = cv2.FONT_HERSHEY_SIMPLEX
    face_path = os.path.join(os.path.dirname(__file__), "classifiers", "haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(face_path) 
    eye_path = os.path.join(os.path.dirname(__file__), "classifiers", "haarcascade_eye.xml")
    eye_cascade = cv2.CascadeClassifier(eye_path)
    cap = cv2.VideoCapture(0) 
    
    switch = False
    thresh = False
    thresh_val=0
    while 1:
        ret, frame = cap.read()
        if window_size:
            frame = cv2.resize(frame, (window_size, window_size))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
        center_point = int(window_size/2)
        cv2.putText(frame,output_text,(center_point,center_point), font, 3, (255,0,0),2, cv2.LINE_AA)     
        for (x,y,w,h) in faces: 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2) 
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray) 
            # Puts rectangle over eyes
            for (ex,ey,ew,eh) in eyes: 
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
            # Logic to check if users face has gone above the threshold value
            if(abs(thresh_val-y)>20 and thresh==True and switch == False):
                switch = True
                output_text = next(word_iter, "Out of words")
            elif(abs(thresh_val-y)<10 and switch==True and thresh==True):
                switch = False
        cv2.imshow('frame',frame) 
        k = cv2.waitKey(30) & 0xff
        if k == ord('q') or k==27: 
            break
        elif k == ord('m'):
            try:
                print('Resetting height to {}px'.format(y))
                thresh_val = y
            except UnboundLocalError:
                print("No face detected")
            thresh = True
    cap.release() 
    cv2.destroyAllWindows() 

    
def main():
    parser = argparse.ArgumentParser(description="Takes input of letters and outputs longest words")
    parser.add_argument("--window_size", default=600, type=int, help="Size of width and height of window")
    parser.add_argument("--letters", required=True, type=str, help="Letters given in anagrams")
    args = parser.parse_args()
    display_words(**vars(args))


if __name__ == "__main__":
    main()

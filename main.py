#!/usr/bin/env python3

import argparse
import os
from pathlib import Path
import time

import dlib
from scipy.spatial import distance as dist
import cv2
from imutils import face_utils

from longest_word import get_longest_words

def eye_aspect_ratio(eye):
    """
    Computes aspect ratio of a given eye

    Args:
        eye ()
    """
    # Distance between each eye's vertical landmarks
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# Euclidean distance between horizontal landmars
	C = dist.euclidean(eye[0], eye[3])

	ear = (A + B) / (2.0 * C)
	return ear


def display_words(window_size: int, letters: str, **kwargs):
    word_list = get_longest_words(letters)
    word_iter = iter(word_list)
    output_text = next(word_iter)
    font = cv2.FONT_HERSHEY_SIMPLEX

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("/home/jdiniso/github/AnagramsCheat/shape_predictor_68_face_landmarks.dat")

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    reset = True
    cap = cv2.VideoCapture(0)
    time_start = 0

    while 1:
        _, frame = cap.read()
        frame = cv2.resize(frame, (1000,1000))
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(img, 0)

        for rect in rects:
            shape = predictor(img, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR+rightEAR) / 2

            if ear < 0.34:
                if not time_start:
                    time_start = time.time() * 1000.
                if time.time() * 1000. - time_start > 5 and reset:
                    output_text = next(word_iter)
                    reset = False
            else:
                reset = True
                time_start = None

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        cv2.putText(frame,output_text,(500,500), font, 3, (255,0,0),2, cv2.LINE_AA)   
        cv2.imshow("img",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
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

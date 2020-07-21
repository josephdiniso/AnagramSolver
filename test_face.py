import dlib
from scipy.spatial import distance as dist
import cv2
from imutils import face_utils






def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)

	# return the eye aspect ratio
	return ear


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/jdiniso/github/AnagramsCheat/shape_predictor_68_face_landmarks.dat")


(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

img = cv2.imread("/home/jdiniso/person.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rects = detector(img, 0)

for rect in rects:
    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
    frame = cv2.imread("/home/jdiniso/person.jpg")
    shape = predictor(img, rect)
    shape = face_utils.shape_to_np(shape)

    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    ear = (leftEAR+rightEAR) / 2

    leftEyeHull = cv2.convexHull(leftEye)
    rightEyeHull = cv2.convexHull(rightEye)
    cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
    cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
    
    cv2.imshow("img",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

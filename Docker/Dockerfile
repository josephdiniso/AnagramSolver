FROM python:3
ADD main.py /
ADD longest_word.py /
ADD shape_predictor_68_face_landmarks.dat /
ADD wordlist.txt /
ADD requirements.txt / 
ADD make_dlib.sh /
RUN apt-get -y update
RUN apt-get install -y build-essential cmake
RUN apt-get install -y libopenblas-dev liblapack-dev
RUN apt-get install -y libx11-dev libgtk-3-dev
RUN apt-get install -y python python-dev python-pip
RUN apt-get install -y python3 python3-dev python3-pip

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]


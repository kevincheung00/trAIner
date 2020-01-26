from flask import Flask, render_template, request
import os
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import time
import dlib
import cv2
import blinkdetect
import emotionsWithVideo
import eyedetect

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, "videos/")
    # print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        # print(file)
        filename = file.filename
        # destination = "/".join([target, filename])
        # print(destination)
        # file.save(destination)
        # print(blinkdetect.main(filename))
    return render_template("complete.html")
    # return ("200")

@app.route("/results")
def calculate():
    numBlinks = blinkdetect.count(filename)
    print(numBlinks)
    pieChart = emotionsWithVideo.getChart(filename)
    pieChart.show()
    eyeCount = eyedetect.getEyeCount(filename)
    print(eyeCount)
    return (eyeCount)


if __name__ == "__main__":
    app.run(host="localhost", port="8080")

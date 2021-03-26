import cv2
import numpy as np
from vehicle_count import *
def main():
    cap = cv2.VideoCapture("video.mp4")
    mainProgram(cap)
main()

import cv2

from flask import Response

import controllers.frames

# region Generate_FrameLayers


def generate_FrameLayer01(name):
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with controllers.frames.lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if (controllers.frames.outputVideolayer01 is None):
                continue

            # encode the frame in JPEG format
            (flag_frame, encodedImage_frame) = cv2.imencode(
                ".jpg", controllers.frames.outputVideolayer01)

            # ensure the frame was successfully encoded
            if not flag_frame:
                continue

            # yield the output frame in the byte format
            ca = "--" + name + "\r\n"

        yield (str.encode(ca) + b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage_frame) + b'\r\n')


def generate_FrameLayer02(name):
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with controllers.frames.lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if (controllers.frames.outputVideolayer02 is None):
                continue

            # encode the frame in JPEG format
            (flag_frame, encodedImage_frame) = cv2.imencode(
                ".jpg", controllers.frames.outputVideolayer02)

            # ensure the frame was successfully encoded
            if not flag_frame:
                continue

            # yield the output frame in the byte format
            ca = "--" + name + "\r\n"

        yield (str.encode(ca) + b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage_frame) + b'\r\n')


def generate_FrameLayer03(name):
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with controllers.frames.lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if (controllers.frames.outputVideolayer03 is None):
                continue

            # encode the frame in JPEG format
            (flag_frame, encodedImage_frame) = cv2.imencode(
                ".jpg", controllers.frames.outputVideolayer03)

            # ensure the frame was successfully encoded
            if not flag_frame:
                continue

            # yield the output frame in the byte format
            ca = "--" + name + "\r\n"

        yield (str.encode(ca) + b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage_frame) + b'\r\n')


def generate_FrameLayer04(name):
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with controllers.frames.lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if (controllers.frames.outputVideolayer04 is None):
                continue

            # encode the frame in JPEG format
            (flag_frame, encodedImage_frame) = cv2.imencode(
                ".jpg", controllers.frames.outputVideolayer04)

            # ensure the frame was successfully encoded
            if not flag_frame:
                continue

            # yield the output frame in the byte format
            ca = "--" + name + "\r\n"

        yield (str.encode(ca) + b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage_frame) + b'\r\n')


def generate_FrameLayer05(name):
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with controllers.frames.lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if (controllers.frames.outputVideolayer05 is None):
                continue

            # encode the frame in JPEG format
            (flag_frame, encodedImage_frame) = cv2.imencode(
                ".jpg", controllers.frames.outputVideolayer05)

            # ensure the frame was successfully encoded
            if not flag_frame:
                continue

            # yield the output frame in the byte format
            ca = "--" + name + "\r\n"

        yield (str.encode(ca) + b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage_frame) + b'\r\n')
# endregion

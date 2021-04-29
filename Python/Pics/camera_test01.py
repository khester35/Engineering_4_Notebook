import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    print("running")
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test2.jpg')
    print("done")

import time
import picamera
effects = ["negative", "solarize", "sketch", "oilpaint", "blur"]
nme = input("enter file name:\n")
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    for i in range(len(effects)):
        camera.image_effect = effects[i]
        print("running")
        # Camera warm-up time
        time.sleep(2)
        camera.capture(nme + effects[i] + ".jpg")
        print("done")
        print("file saved as: "+nme + effects[i] + ".jpg\n")

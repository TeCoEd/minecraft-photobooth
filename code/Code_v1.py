import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
import picamera

###Code to take a picture###
###@TeCoEd###
def take_the_pic():
    with picamera.PiCamera()as camera:
        #camera.resolution = (150, 100)
        camera.start_preview()
        time.sleep(2)
        camera.capture('selfie.jpg')

def where_am_I():
    while True:
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z
    #print x, y, z
        time.sleep(3)
        if x >= 10.5 and y == 9.0 and z == -44.3:
        #print "You are at the photobooth!"
        
            mc.postToChat("You are in the Photobooth!")
            time.sleep(1)
            mc.postToChat("Smile!")
            time.sleep(1)
            take_the_pic()
            mc.postToChat("Check out your picture")
            time.sleep(5)
        else:
            pass

def start():
    mc.postToChat("Find the Photo-Booth")
    where_am_I()
    
start()

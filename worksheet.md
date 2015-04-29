# Minecraft Photobooth

Create a photobooth in Minecraft which when the player enters it triggers the PiCamera and takes you picture

## The First Step

The first step is to attach the PiCamera.  This is covered in this tutorial.  Once you have connected the camera boot up the Raspberry Pi

1. Open the LX Terminal

2. Type sudo halt

This will load the Python IDLE code editor which you will use to write the Photobooth program

## Step two

1. The first part of the program is to import the Minecraft API. (Application Programming Interface) This enables you to connect to Minecraft and use Python to code.
   In the new IDLE window type the following code, which will import the PiCamera module and the time module.    
   
	``` python
    import mcpi.minecraft as minecraft
	mc = minecraft.Minecraft.create()
	import time
	import picamera
	```
## Step three

Next we need to create a function which will control the PiCamera.  A function is a set of code lines which can do something but may take several lines of code to do this.
By creating a function you can use a short word or phrase to call the lines of code.  In the code below it triggers the PiCamera every time the take_the_pic()     

	``` python
	def take_the_pic():
    with picamera.PiCamera()as camera:
        #camera.resolution = (150, 100)
        camera.start_preview()
        time.sleep(2)
        camera.capture('selfie.jpg')
	``` 	

1. Now do D

1. Now do X

Now we have X

## The Next Step

Now we've done X, we'll do Y.

1. First do A

1. Then do B

1. Now do C in code:

    ```python
    print("Hello world")
    ```

    In Python the `print` function is something

1. Now do D

1. Now do Y

Now we have X and Y

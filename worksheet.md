# Minecraft Photo booth

Create a Photo booth in Minecraft, which you the player enter the Photo booth it triggers the PiCamera and takes your picture, don't forget to smile.

## The First Step

The first step is to attach the PiCamera.  This is covered in this tutorial.  Once you have connected the camera boot up the Raspberry Pi

1. Open the LX Terminal

2. Type sudo idle

This will load the Python IDLE code editor which you will use to write the Photo booth program

## Importing the Minecraft API

The first part of the program is to import the Minecraft API. (Application Programming Interface) This enables you to connect to Minecraft and use Python to code.
In the new IDLE window type the following code.  This will import the PiCamera module to control the camera and the time module to add a small delay between
taking the photo and then taking the next photo.    
   
``` python
from mcpi import minecraft​
​mc = minecraft.Minecraft.create()
import time
import picamera
```

## A function to control the PiCamera

Next we need to create a function which will control the PiCamera.  A function is made up of a number of lines of code which do something but may take several lines of code to do this.
By creating a function you can use a short word or phrase to call the lines of code.  In the code below it triggers the PiCamera every time the take_the_pic()     

``` python
def take_the_pic():
	with picamera.PiCamera()as camera:
		#camera.resolution = (150, 100)
		camera.start_preview()
		time.sleep(2)
		camera.capture('selfie.jpg')
``` 	
We have set the camera to show a two second preview so that you can strike your pose and smile before the picture is taken.  The camera stores the image in
a file called selfie.jpg

## Where am I?

When you are playing Minecraft your the program will need to test if you are inside the Photo booth, then it will trigger the take_the_pic function and take a picture.
To do this Minecraft needs to know where you are in the world, it needs to measure your position.  In the Minecraft environment your position is measured in the
X, Y and Z axis.  To find your position you use the code, pos = mc.player.getPos().  This measures the X, Y , Z position of your player.  You can then use
print pos.x to print the X value.  Now you now the position of the player you can test to see if they are in the Photo booth. 

``` python
def where_am_I():
	while True:
		pos = mc.player.getPos()
		x = pos.x
		y = pos.y
		z = pos.z
```
	
## Building a Photo booth Part 1

Now we need to create a Photo booth in the Minecraft environment, this is done manually and can be built where ever you want to locate it.  To open Minecraft, 

1. Click the start button

2. Select games / coding and Minecraft.  

3. When it opens create a new world.

Using any block type create a Photo booth, ideally this should have one block of free space inside so that the player can enter.

## Building a Photo booth Part 2

Once you have created your Photo booth move the player inside and onto the block where you want to trigger the PiCamera.  In the top right of the window 
you will see the X, Y, Z co-ordinates of your player, for example 10.5, 9.0, -44.3.  These are the X, Y, Z, co-ordinates of the 'trigger' block in your Photo booth,
 
1. Walk into your Photo booth

2. Record the X, Y, Z co-ordinates of your PiCamera 'trigger' block.

## Testing that you are in the Photo booth 
 
At this point we have a Photo booth, the co-ordinates of the trigger block, and a function to control the PiCamera and take a picture.  The next step is to test the program 
identifies when you are in the Photo booth.  To do this we must create a loop which checks if your player co-ordinates match the trigger block co-ordinates. If they
do then you are standing in the Photo booth.  You can do this by using a simple if statement, we call these conditionals.  Add the code below to your Python program. 

```python
while True:
	where_am_I()
	time.sleep(2)
	if x >= 10.5 and y == 9.0 and z == -44.3:
		print "You are at the Photo booth!"   
where_am_I()		
```

1. Save the program and press F5 to test it.

2. Walk into the Photo booth

You will note that the if statement checks if x is greater than or equal to 10.5, this is ensure that it picks up the block as it could have a value of 10.6.

## Putting it all together Part 1

Now you have a working Photo booth we just need to add the PiCamera to take a picture.   We will replace the console message with a message in Minecraft 
to tell you that you are in the Photo booth, A quick reminder to smile and then call the PiCamera function, take_the_pic()  T
 
1. Comment out the print "You are at the Photo booth!"   

2. Under and in line with the You are at the Photo booth, add the following code

```python
mc.postToChat("You are in the Photo booth!")
time.sleep(1)
mc.postToChat("Smile!")
time.sleep(1)
take_the_pic()
mc.postToChat("Check out your picture")
time.sleep(5)
```

3. Delete the where_am_I() line	
	
## What if you are not in the Photo booth?

What happens if you are not inside the Photo booth, this needs to be coded as well.  We will use an else statement, which will run of the if statement does not run.
if you are in the Photo booth then take the picture else (if not) then do something else.  We want if to pass and then check again to see if you are in the Booth yet.

1. Under the time.sleep(5) and in line with the if statement add the following code

```python
else:
	pass
```

## Putting it all together Part 2

Well done you are nearly there, the final part of the project is to create one more function to begin the program and run the other functions that check where you are.
You will notice now that your original where_am_I() function includes all the code to check the players location and trigger the camera.  A new function will call
these parts of the program

1. Add the code below to the bottom of your program

```python
def start():
    mc.postToChat("Find the Photo-Booth")
    where_am_I()
    
start()
```

2. Save the program

3. Press F5 to run and test the Photo booth

## What next

1. Add a specific block which triggers the camera

2. Add further blocks to control PiCamera settings such as taking a video or applying a filter 


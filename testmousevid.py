from PIL import Image
import PIL.ImageGrab
import keyboard
import time
import pyautogui
import cv2
import pyscreenshot
"""first thing that you need to find out where is your virtual screen is located on your monitor screen. If its pixels
are located precisely of each other then just find out coordinates of center of every lamp in each corner, use for this 
21th line.
    All code down there is two cycles in one big. One big is running through your amount of frames, first little turning 
necessery lamps on and second little turning it off.
    Use online convertors to get frame sequance of your video and compress every frame to resolution you using for virtual
screen. put them all in one folder named as "storage2" like in this code or change its name here. every frame you got will
be screenshoted and saved in another folder named as "result2". then put them all together in video redactor (adobe premire
is most convenient). Change 28th and 43th line as you want files to be named and counted
    If your not sure whether your virtual screen is perfect write separate code using pyautogui library and check how it
goes from first lamp to last of every row."""
time.sleep(10) #gives you some time to move to desired application window

print(pyautogui.displayMousePosition) #use this to indicate cursor coordinates

for k in range(300): #amount of video's frames containing in storage2/
    x=67 #coordinates of center of pixel in upper left corner of your virtual screen MINUS range in 34th line
    y=39 #coordinates of center of pixel in upper left corner of your virtual screen MINUS range in 31th line
    
    im = cv2.imread('storage2/split_video007_'+str(k//100)+str(k//10%10)+str(k%10)+'.jpg',cv2.IMREAD_GRAYSCALE)
    im2=cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)[1] #turns original frame into more clear one (only black and white)
    
    for i in range(34): #rows
        y = y + 21        #range in pixels between two rows
        for j in range(44): #columns
            if x>=991: #coordinates of last pixel in the row
                x = 88 #if row is over it goes to next one
            else:
                x=x+21   #range in pixels between two lamps in the row
            if im2[i][j]==255:
                pyautogui.moveTo(x,y) #going to coordinates of current lamp
                keyboard.send('f') #turning it on by typing f (in people playground)
    
    pyautogui.moveTo(1200,500) #so mouse wont bother you on screenshot
    im1=pyscreenshot.grab()
    im1.save('result2/kadrfin1_'+str((k+2100)//100)+str((k+2100)//10%10)+str((k+2100)%10)+'.jpg')
    
    x=67 #returning back
    y=39
    
    for i in range(34):
        y = y + 21
        for j in range(44):
            if x>=991:
                x = 88
            else:
                x=x+21
            r1,g1,b1=PIL.ImageGrab.grab().load()[x,y] #brightness of current pixel
            if r1>100 and g1>100 and b1>100: #if it's bright enough (means it is turned on) turns it off, making all frame clear for next one
                pyautogui.moveTo(x,y)
                keyboard.send('f') #same hotkey that turns lamp off

keyboard.send('esc') #sign that your code is completed all frames (here it pauses the game)

#########################################################################
#Pra Soft AUTOMATOR v0.1 (cli-version)                                  #
#Copywrites(C)2025 Copywrites Reserved Pracorp 2025                     #
#########################################################################
from pynput import mouse 
from pynput import keyboard 
import pyautogui
import pynput
import os
import time
import string
import sys
#______________________(Global variables)________________________________#
store=[]     
count=-1
clicktime=[]
sec=[]
sec1=''
movecount=-1
movesec=[]
movetime=[]
movelist=[]
stopped=False
choice=1
#_______________________(Startup)________________________________________#

print("Welcome program automation software(prasoft)")
print("press ctrl and b to stop recording")
filename=input("Enter a name to save your automation :")
filename+=(".py")
file=open(filename,mode='a')
no_spaces=62-len(filename)
print(no_spaces)
for i in range(0,no_spaces):
 filename+=' '
h1="#########################################################################\n"
h2="#Pra Soft AUTOMATOR v0.1(cli-version) )-->(Mchine Generated Python Code)#\n"
h3="#Copywrites(C)2025 Reserved Pracorp 2025                                #\n"
hf="#Filename:{0}#\n".format(filename)
h4="#########################################################################\n"
a="from pynput.mouse import Button, Controller as mousecontroller"
f="from pynput.keyboard import Key, Controller as keyboardcontroller"
q="mouse=mousecontroller()"
b="import time,pyautogui"
c='c=input("do you want to continue:")'
d="if c=='y':"
e="    time.sleep(5)"
time.sleep(2)
file.write(h1)
file.write(h2)
file.write(h3)
file.write(hf)
file.write(h4)
file.write(a)
file.write('\n')
file.write(f)
file.write('\n')
file.write(b)
file.write('\n')
file.write(q)
file.write('\n')
file.write("keyboard=keyboardcontroller()")
file.write('\n')
file.write(c)
file.write('\n')
file.write(d)
file.write('\n')
file.write(e)
file.write('\n')
file.close()

#_____________________________(mouse)_______________________________________#

def on_click(x, y, button, pressed):
 if stopped==False:
          print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
          print(time.perf_counter())
         
          #store.append("    mouse.position =({0},{1})".format(x,y))
          global clicktime
          global count
          global sec
          global sec1
          count=count+1

          if count==0:
              clicktime.append(time.perf_counter())
        
          if count>=1:
                  clicktime.append(time.perf_counter())
                  sec1=clicktime[count]-clicktime[count-1]
                  sec.append(sec1)
                  print(button)
                  buttonname=button
                  file=open(filename,mode='a')
                 # file.write(store[count])
                 # file.write('\n')
                  if pressed:
                      file.write("    mouse.press({0})#Press {0}".format(buttonname))
                      file.write('\n')
                      file.write("    time.sleep({0})#Sleeps for {0} seconds".format(sec[count-1]))
                      file.write('\n')
                  if not pressed:
                      file.write("    mouse.release({0})#Releases {0}".format(buttonname))
                      file.write('\n')
                      file.write("    time.sleep(0.00001)#Sleeps for 0.00001 seconds")
                      file.write('\n')
                  file.close()
        
          else:
             pass
  
         
 
def on_scroll(x, y, dx, dy):
        if stopped==False:

              print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
              scrollist=[]
              if dy<0:
                   scrollist.append("    pyautogui.scroll({0},{1},{2})".format(-100,x,y))
                   
              else:
                   scrollist.append("    pyautogui.scroll({0},{1},{2})".format(100,x,y))
              file=open(filename,mode='a')
              file.write(scrollist[0])
              file.write('\n')
              file.write("    time.sleep(0.000000001)")
              file.write('\n')
              file.close()
def on_move(x, y):
    if stopped==False: 
      print('Pointer moved to {0}'.format((x, y)))
      global count
      count=count+1
      global movelist
      movelist.append("    mouse.position =({0},{1})".format(x,y))
      global sec,clicktime,sec1,control,control1
      control=0
      control1=0
      if count==0:
           clicktime.append(time.perf_counter())
           file=open(filename,mode='a')
           file.write(movelist[len(movelist)-1])
           file.write('\n')
           file.write("    time.sleep(0.00001)")
           file.write('\n')
           file.close()

      if  count>=1:
                    clicktime.append(time.perf_counter())
                    sec1=clicktime[count]-clicktime[count-1]
                    sec.append(sec1)
                    file=open(filename,mode='a')
                    file.write(movelist[len(movelist)-1])
                    file.write('\n')
                    file.write("    time.sleep({0})".format(sec[count-1]))
                    file.write('\n')
                    file.close()

#_____________________________(keyboard)______________________________________________#
def on_press(key):
 try:
    global stopped
    if stopped==False:
           if key.char=='\x13':
                  file=open(filename,mode='a')
                  file.write("    keyboard.press(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  file.write("    keyboard.press('s')")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+s is pressed")
                  file.close()
           if key.char=='\x13':
               file=open(filename,mode='a')
               file.write("    keyboard.press('s')")
               file.write('\n')
               file.write("    time.sleep(0.01)")
               file.write('\n')
               file.write("    keyboard.release(Key.ctrl_l)")
               file.write('\n')
               file.write("    time.sleep(0.01)")
               file.write('\n')
               print("ctrl+s is released")
               file.close()
           if key.char=='\x1a':
               file=open(filename,mode='a')
               file.write("    keyboard.press('z')")
               file.write('\n')
               file.write("    time.sleep(0.01)")
               file.write('\n')
               file.write("    keyboard.release(Key.ctrl_l)")
               file.write('\n')
               file.write("    time.sleep(0.01)")
               file.write('\n')
               print("ctrl+z is released")
               file.close()
           if key.char=='\x18':
               file=open(filename,mode='a')
               file.write("    keyboard.press('x')")
               file.write('\n')
               file.write("    time.sleep(0.01)")
               file.write('\n')
               file.write("    keyboard.release(Key.ctrl_l)")
               file.write('\n')
               file.write("    time.sleep(0.01)")
               file.write('\n')
               print("ctrl+x is released")
               file.close()
           if key.char=='\x03':
                  file=open(filename,mode='a')
                  file.write("    keyboard.press('c')")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  file.write("    keyboard.release(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+c is released")
                  file.close()
           if key.char=='\x16':
                  file=open(filename,mode='a')
                  file.write("    keyboard.press('v')")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  file.write("    keyboard.release(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+v is released")
                  file.close()
           if key.char=='\x02':
                  file=open(filename,mode='a')
                  file.write("    #keyboard.press('b')")
                  file.write('\n')
                  file.write("    #time.sleep(0.01)")
                  file.write('\n')
                  file.write("    #keyboard.release(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    #time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+b is released")
                  file.close()
           if key.char=='\x0e':
                  file=open(filename,mode='a')
                  file.write("    keyboard.press('n')")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  file.write("    keyboard.release(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+n is released")
                  file.close()
           if key.char=='\r':
                  file=open(filename,mode='a')
                  file.write("    keyboard.press('m')")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  file.write("    keyboard.release(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+m is released")
                  file.close()
           if key.char=='\x04':
                  file=open(filename,mode='a')
                  file.write("    keyboard.press('d')")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  file.write("    keyboard.release(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+d is released")
                  file.close()
           if key.char=='\x06':
                  file=open(filename,mode='a')
                  file.write("    keyboard.press('f')")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  file.write("    keyboard.release(Key.ctrl_l)")
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  print("ctrl+f is released")
                  file.close()
           else:
                  print(type(key))
                  print(key)
                  print('alphanumeric key {0} pressed'.format(key))
                  presskeylist=[]
                  keylog=[]
                  presskeylist.append("    keyboard.press('{0}')".format(key.char))
                  file=open(filename,mode='a')
                  file.write(presskeylist[0])
                  file.write('\n')
                  file.write("    time.sleep(0.01)")
                  file.write('\n')
                  global control
                  control=0
                  file.close()
 except AttributeError:
                 print('special key {0} pressed'.format(key))
                 splpresskeylist=[]
                 splpresskeylist.append("    keyboard.press({0})".format(key))
                 file=open(filename,mode='a')
                 file.write(splpresskeylist[0])
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 control=0
                 file.close()
def on_release(key):
        try:
           global stopped
           if stopped==False:
             if key.char=='\x13':
                 file=open(filename,mode='a')
                 file.write("    keyboard.release('s')")
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 file.write("    keyboard.release(Key.ctrl_l)")
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 print("ctrl+s is released")
                 file.close()
             if key.char=='\x1a':
                 file=open(filename,mode='a')
                 file.write("    keyboard.release('z')")
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 file.write("    keyboard.release(Key.ctrl_l)")
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 print("ctrl+z is released")
                 file.close()
             if key.char=='\x18':
                 file=open(filename,mode='a')
                 file.write("    keyboard.release('x')")
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 file.write("    keyboard.release(Key.ctrl_l)")
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 print("ctrl+x is released")
                 file.close()
             if key.char=='\x03':
                    file=open(filename,mode='a')
                    file.write("    keyboard.release('c')")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    file.write("    keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+c is released")
                    file.close()
             if key.char=='\x16':
                    file=open(filename,mode='a')
                    file.write("    keyboard.release('v')")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    file.write("    keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+v is released")
                    file.close()
             if key.char=='\x02':
                    file=open(filename,mode='a')
                    file.write("    #keyboard.release('b')")
                    file.write('\n')
                    file.write("    #time.sleep(0.01)")
                    file.write('\n')
                    file.write("    #keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    #time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+b is released")
                    file=open(filename,mode='a')
                    print("mouse and keyboard listener has been stopped")
                    stopped=True
                    record(stopped)
                    file.close()
             if key.char=='\x0e':
                    file=open(filename,mode='a')
                    file.write("    keyboard.release('n')")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    file.write("    keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+n is released")
                    file.close()
             if key.char=='\r':
                    file=open(filename,mode='a')
                    file.write("    keyboard.release('m')")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    file.write("    keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+m is released")
                    file.close()
             if key.char=='\x04':
                    file=open(filename,mode='a')
                    file.write("    keyboard.release('d')")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    file.write("    keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+d is released")
                    file.close()
             if key.char=='\x01':
                    file=open(filename,mode='a')
                    file.write("    keyboard.release('a')")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    file.write("    keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+a is released")
                    file.close()
             if key.char=='\x06':
                    file=open(filename,mode='a')
                    file.write("    keyboard.release('f')")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    file.write("    keyboard.release(Key.ctrl_l)")
                    file.write('\n')
                    file.write("    time.sleep(0.01)")
                    file.write('\n')
                    print("ctrl+f is released")
                    file.close()
             if key.char=='\x02':
                          file=open(filename,mode='a')
                          file.write("\n ##################################################################(end-of-file)###########################################################")
                          file.close()
                          
             else:
                 print('{0} released'.format(key.char))
                 releasekeylist=[]
                 releasekeylist.append("    keyboard.release('{0}')".format(key.char))
                 file=open(filename,mode='a')
                 file.write(releasekeylist[0])
                 file.write('\n')
                 file.write("    time.sleep(0.01)")
                 file.write('\n')
                 file.close()

        except AttributeError:
           if stopped==False:
              print('special key {0} released'.format(key))
              splreleasekeylist=[]
              splreleasekeylist.append("    keyboard.release({0})".format(key))
              file=open(filename,mode='a')
              file.write(splreleasekeylist[0])
              file.write('\n')
              file.write("    time.sleep(0.01)")
              file.write('\n')
              control1=0
              file.close()

listener=keyboard.Listener(
on_press=on_press,
on_release=on_release)
listener.start()
with mouse.Listener(
on_move=on_move,
on_click=on_click,
on_scroll=on_scroll) as listener1:
      listener1.join()


         


      





          



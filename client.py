import time
from pythonosc.udp_client import SimpleUDPClient

import numpy as np
import pyautogui



# Constants
ip = "127.0.0.1"
port = 9000 #1337

# int addresses
address_emote = "/avatar/parameters/VRCEmote"
address_face = "/avatar/parameters/Face"
address_viseme = "/avatar/parameters/Viseme"
address_gesture_left = "/avatar/parameters/GestureLeft"
address_gesture_right = "/avatar/parameters/GestureRight"
address_bodygrab = "/avatar/parameters/BodyGrab"
address_tails = "/avatar/parameters/Tails"
address_tracking_type = "/avatar/parameters/TrackingType"
address_mute_self = "/avatar/parameters/MuteSelf"

# Boolean addresses
address_is_headpatted = "/avatar/parameters/is_headpatted"
address_nose_boop = "/avatar/parameters/Nose_boop"
address_blink = "/avatar/parameters/blink"
address_d1 = "/avatar/parameters/D1"
address_booba = "/avatar/parameters/Booba"
address_dress = "/avatar/parameters/Dress"
address_go_pose = "/avatar/parameters/Go/Pose"

# Float addresses
address_vrcfaceblendv = "/avatar/parameters/VRCFaceBlendV"
address_vrcfaceblendh = "/avatar/parameters/VRCFaceBlendH"

value = 1

# Create client
client = SimpleUDPClient(ip, port)

def loop_messages(
        address: str = address_emote,
        sleep_time: int = 3,
        start_value: int = 0,
        end_value: int = 26,
        step: int = 1):
    """Send messages to the server."""
    for x in range(start_value,end_value, step):
        client.send_message(address, x)
        print("Sent message to {} with value {}".format(address, x))
        time.sleep(sleep_time)

def loop_messages_float(
        addressv: str = address_emote,
        addressh: str = address_emote,
        sleep_time: int = 1):
    """Send messages to the server."""
    for x in np.arange(-1, 1.1, 0.1):
        client.send_message(addressv, x)
        client.send_message(addressh, x)
        print("Sent message to {} with value H={}".format(addressv, x))
        time.sleep(sleep_time)

def send_chatbox_message(text: str = "Hello World!"):
    """Send a message to the chatbox."""
    # Send message
    address = "/chatbox/input"
    client.send_message(address, [text, True, False])

def main():
    #send_chatbox_message("Hola, como estan?")
    # addressv = "/avatar/parameters/VRCFaceBlendV"
    # addressh = "/avatar/parameters/VRCFaceBlendH"
    # # Coordinates: -1, -1 is bottom left, 1, 1 is top right
    # # Bottom left


    # client.send_message("/avatar/parameters/GestureLeftWeight", 0.95)
    # client.send_message("/avatar/parameters/GestureRightWeight", 0.95)
    send_chatbox_message("Testing GestureLeft")
    loop_messages(
        address="/avatar/parameters/GestureLeft",
        sleep_time=1,
        start_value=0,
        end_value=8,
    )

    send_chatbox_message("Testing GestureRight")
    loop_messages(
        address="/avatar/parameters/GestureRight",
        sleep_time=1,
        start_value=0,
        end_value=8,
    )


    #loop_messages(address="/avatar/parameters/GestureLeft", sleep_time=1)
    time.sleep(3)
    # pyautogui.move(400, 0) # move mouse 10 pixels down
    # pyautogui.keyDown('w')
    # time.sleep(3)
    # pyautogui.typewrite('Hello world!\n', interval=.5)  # useful for entering text, newline is Enter
    # pyautogui.keyUp('w')
    # pyautogui.keyDown('shiftleft')
    # time.sleep(1)
    # pyautogui.keyDown('f2')
    # time.sleep(1)
    # pyautogui.keyUp('f2')
    # time.sleep(1)
    # pyautogui.keyDown('f1')
    # time.sleep(1)
    # pyautogui.keyUp('f1')
    # time.sleep(1)
    # pyautogui.keyUp('shiftleft')


if __name__ == "__main__":
    main()
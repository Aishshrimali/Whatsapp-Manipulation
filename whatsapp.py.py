# Importing the Pyautogui Library for automating GUI interactions
import pyautogui

# Importing the Requests Library for making HTTP requests
import requests

# Initializing an empty list to store contact numbers
con_list=[]

# Taking user input for name, contact, and message
name1 = input("Enter name:")
contact1 = input("Enter contact:")
msg1 = input("Enter msg:")

# Sending a GET request to a local server to save the message details
r = requests.get("http://localhost/msg.php?name=" + name1 + "&contact=" + contact1 + "&msg=" + msg1)

# Starting an infinite loop to repeatedly fetch and process messages
while True:
    # Sending a GET request to fetch messages from the local server
    r = requests.get("http://localhost/fetch.php?sent=sent")
    a = r.text  # Storing the response text

    # Finding the position of the word "warning" in the response text
    b = a.find("warning")
    print(b)  # Printing the position (index) of "warning"

    # If "warning" is found in the response text
    if b > 0:
        print("msg not available")
    else:
        # Adding the response text to the contact list and splitting it by commas
        con_list.append(a)
        con_list = a.split(",")
        print("con_list:", con_list)

        # Extracting the last 10 characters (assumed to be the contact number)
        b = con_list[0]
        c = b[-10:]
        con_list.pop(0)  # Removing the first element from the contact list
        con_list.append(c)  # Adding the extracted contact number to the contact list
        print("contact_no:", con_list)

        # Removing the contact number from the message text
        remaining_txt = b.strip()
        msg = remaining_txt[:-10].strip()
        print("msg:", msg)

        # Simulating pressing "alt + tab" to switch windows
        pyautogui.hotkey("alt", "tab")

        # Looping through each contact in the contact list
        for i in range(len(con_list)):
            # Moving the mouse to a specific position and clicking to focus on an input field
            pyautogui.moveTo(200, 240, duration=7, tween=pyautogui.easeInOutQuad)
            pyautogui.click()

            # Typing the contact number and message, then pressing "enter"
            pyautogui.write(con_list[i])
            pyautogui.press("enter")
            pyautogui.write(msg)
            pyautogui.press("enter")

            # Checking the status code of the response to handle errors
            if r.status_code == 404:
                print("File not found")
            elif r.status_code == 200:
                print(r.text)  # Printing the response text if the request was successful

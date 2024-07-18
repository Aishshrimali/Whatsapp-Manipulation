import pyautogui
import requests
con_list=[]
name1 = input("Enter name:")
contact1 = input("Enter contact:")
msg1 = input("Enter msg:")

r = requests.get("http://localhost/msg.php?name="+name1+"&contact="+contact1+"&msg="+msg1)

while True:
    r = requests.get("http://localhost/fetch.php?sent=sent")
    #r = requests.get("http://192.168.1.22/fetch.php?sent=sent")
    a = r.text
    #print("a:",a)
    
    b = a.find("Warning")
    print(b) 
    
    if b > 0 :
    
        print("msg not avilable")
        
    else:
        con_list.append(a)
        con_list=a.split(",")
        print("con_list:",con_list)

        b = con_list[0]
    
        c = b[-10:]
        con_list.pop(0)
        con_list.append(c)
        print("contact_no:",con_list)
            
        remaining_txt = b.strip()
            
        msg = remaining_txt[:-10].strip()
        print("msg:",msg)  
        
        pyautogui.hotkey("alt","tab")
            
        i=0
        for i in range (len(con_list)):
        
            pyautogui.moveTo(200, 240, duration=7, tween=pyautogui.easeInOutQuad)
            #pyautogui.hotkey("ctrl","alt","/")
            pyautogui.click()
            pyautogui.write(con_list[i])
            pyautogui.press("enter")
            pyautogui.write(msg)    
            pyautogui.press("enter")
                            
            #i=i+1
                 
            if r.status_code == 404:
                print("File not found")
            elif r.status_code == 200:
                #print("Data inserted successfully")
                print(r.text)
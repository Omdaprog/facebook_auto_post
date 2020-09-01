
import pyautogui
import time

groups = ["soussssse/", "443244755735802/", "vente.et.achat.a.sousse.islem", "511173708907339", "693214307504644",
          "1390166881296565", "bi3wechri2", "stop", "ventemonastirsoussemahdia", "MaCanDoProd", "echrifisoussa", "204689443015734"]

time.sleep(5)


cnt = 0
for i in groups:
    if i == "stop":
        user = input("waiting")
        if user == "start":
            print("yes sir")
    else:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('t')
        pyautogui.keyUp('t')
        pyautogui.keyUp('ctrl')
        link = "https://www.facebook.com/groups/" + i
        pyautogui.typewrite(link)
        pyautogui.typewrite("\n")
        print(cnt+1)

        while True:
            location = pyautogui.locateCenterOnScreen('vendre.PNG')
            if location == None:
                print('still loocking for it')
            else:
                pyautogui.click(x=location[0], y=location[1])
                break

        while True:
            location = pyautogui.locateCenterOnScreen('Ajouter des photos.PNG')
            if location == None:
                print('still loocking for <Ajouter des photos.PNG>')
            else:
                pyautogui.click(x=location[0], y=location[1])
                break

        time.sleep(1)
        print("typing scooter electrique")
        pyautogui.typewrite("scooter electrique")
        pyautogui.press("enter")

        time.sleep(1)
        while True:
            location = pyautogui.locateCenterOnScreen(
                'Ajouter une autre photo.PNG')
            if location == None:
                print('still loocking for it')
            else:
                pyautogui.click(x=location[0], y=location[1])
                break

        time.sleep(1)
        print("typing scooter electrique")
        pyautogui.typewrite("scooter electrique 2")
        pyautogui.press("enter")

        time.sleep(0.1)
        print("press tab")
        pyautogui.press("tab")
        time.sleep(0.2)

        print("typing scooter electrique")
        pyautogui.typewrite("scooter electrique a vendre")
        time.sleep(0.2)

        print("press tab")
        pyautogui.press("tab")
        time.sleep(0.2)

        print("typing 3000")
        pyautogui.typewrite("3000")
        time.sleep(0.2)

        print("press tab")
        pyautogui.press("tab")
        time.sleep(0.2)

        print("typing discription")
        pyautogui.typewrite(
            "scooter electrique a vendre importer de france en bonne etat \n prix 3000 \n dispo a msaken sousse \n num 52729722 ")
        time.sleep(1)

        print("scroll down")
        pyautogui.scroll(-1000)
        time.sleep(1)

        print("press tab")
        pyautogui.press("tab")
        time.sleep(0.1)

        print("typing scooter electrique")
        pyautogui.typewrite("scooter electrique")
        time.sleep(0.1)
        print("press enter")
        pyautogui.press("enter")

        while True:
            location = pyautogui.locateCenterOnScreen('suivant.PNG')
            if location == None:
                print('still loocking for it')
            else:
                pyautogui.click(x=location[0], y=location[1])
                break
        time.sleep(1)
        pyautogui.scroll(-100000)
        time.sleep(0.1)

        while True:
            location = pyautogui.locateCenterOnScreen('Publier.PNG')
            if location == None:
                print('still loocking for it')
            else:
                pyautogui.click(x=location[0], y=location[1])
                break

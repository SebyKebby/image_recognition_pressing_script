import pyautogui
import time
 
print('Press Ctrl-C to quit.')
 
try:
    while True:
        try:
            directory = os.listdir(r'F:\wababjack')
            for images in directory : 
                if images.endswith('png') :
                    coordinates = pyautogui.locateOnScreen(images)
                    X, Y = pyautogui.center(images)
                    pyautogui.moveTo(X, Y, 0.2)
                    pyautogui.click()
                    print(f"[{time.strftime('%H:%M:%S', time.localtime())}] Clicked on the button. Sleeping for 5 seconds.")
                    time.sleep(5)  # Optional: Add a delay to reduce CPU usage, clicking "Slow Download" makes you wait for 5 seconds
                else:
                    print("Image not found, continuing...")    
        except pyautogui.ImageNotFoundException:
            print(f"[{time.strftime('%H:%M:%S', time.localtime())}] Image not found exception caught. Continuing...")
            time.sleep(1)
except KeyboardInterrupt:
    print('\nScript stopped by user')


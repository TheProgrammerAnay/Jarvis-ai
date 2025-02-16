import webbrowser
import time
import pyautogui

def handle_tracking_code():
    # Prompt the user to enter the tracking code
    tracking_code = input("Enter Tracking Code: ")
    
    # URL of Grabify
    web = "https://grabify.link/"
    
    # Open the web browser and navigate to Grabify
    webbrowser.open(web)
    
    # Wait for the page to load
    time.sleep(8)
    
    # Click on the input field (coordinates might need adjustment based on your screen)
    pyautogui.click(669, 521)
    
    # Type the tracking code into the input field
    pyautogui.typewrite(tracking_code)
    
    # Wait a bit
    time.sleep(5)
    
    # Click on the submit button (coordinates might need adjustment based on your screen)
    pyautogui.click(1032, 594)

# Usage example
query = "tracking code"  # Example query input

if "tracking code" in query:
    handle_tracking_code()

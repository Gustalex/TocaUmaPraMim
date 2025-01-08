import pyautogui
import time
import keyboard
import pygetwindow as gw
from music_selection import get_music_selection

def open_discord_web():
    
    windows = gw.getWindowsWithTitle('Google Chrome')
    
    if windows:
        window = windows[0]
        window.activate()
        time.sleep(1)
        
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        pyautogui.typewrite('https://discord.com/channels/721884428233605130/758417349559844866')
        pyautogui.press('enter')
        time.sleep(7)
    
def send_messages():
    playlist_id = '1ov6f0iKgAIbpyU47zOMwR'
    music_selection = get_music_selection(playlist_id)
    
    for song in music_selection:
        keyboard.write(song)
        keyboard.press_and_release('enter')
        time.sleep(3)
        keyboard.press_and_release('ctrl + enter')
        time.sleep(3)
    
   
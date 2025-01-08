import time
from discord_handler import open_discord_web, send_messages

def main():
    open_discord_web()
    time.sleep(5)
    send_messages()
    
if __name__ == '__main__':
    main()
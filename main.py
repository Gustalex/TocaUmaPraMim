import time
from discord_handler import open_discord_web, send_messages

def main():
    playlist_id = '1qpLP8Zn0wXZ5wxC3nmdVk'
    
    open_discord_web()
    while True:
        print('Randomized Playlist? (y/n)')
        randomize = input().lower()
        if randomize in ['y', 'n']:
            break
        print("Por favor, insira 'y' para sim ou 'n' para não.")
    time.sleep(20)
    send_messages(playlist_id, randomize)

if __name__ == '__main__':
    main()
import tkinter as tk
from tkinter import Button, Entry, Label
import threading
import webbrowser
import sys
from lib.bot import start_bot, stop_bot
from lib.config import load_config
from lib.handlers import setup_handlers

# Global variable to keep track of the bot thread
bot_thread = None

DEFAULT_HOST = 'semcheats.aternos.me'
DEFAULT_PORT = '57717'


def _run_bot_safe(host, port, username, config, auth='offline', version=''):
    """Runs start_bot and prints readable errors instead of crashing silently in threads."""
    try:
        start_bot(host, port, username, config, setup_handlers, auth, version)
    except Exception as err:
        print(f"Failed to start bot: {err}")


def start_bot_thread(host, port, username, config, auth='offline', version=''):
    """
    Starts the bot in a new thread if not already running.

    Args:
        host (str): The server host.
        port (int): The server port.
        username (str): The bot's username.
        config (dict): Configuration for the bot.
        auth (str): Authentication mode ('offline' or 'microsoft').
        version (str): Optional minecraft version (example: 1.20.4).
    """
    global bot_thread
    if bot_thread is None or not bot_thread.is_alive():
        bot_thread = threading.Thread(
            target=_run_bot_safe,
            args=(host, port, username, config, auth, version),
            daemon=True
        )
        bot_thread.start()


def stop_bot_thread():
    """
    Stops the bot and terminates the bot thread.
    """
    global bot_thread
    if bot_thread is not None:
        stop_bot()  # Gracefully disconnect the bot from the server
        bot_thread.join()  # Ensure the thread is properly terminated
        bot_thread = None  # Reset the bot_thread variable


def create_ui():
    """
    Creates the Tkinter GUI for the bot.
    """
    root = tk.Tk()
    root.geometry('365x250')
    root.configure(background='#F0F8FF')
    root.title('Minecraft Bot')

    host = Entry(root)
    host.insert(0, DEFAULT_HOST)
    host.place(x=165, y=20)

    port = Entry(root)
    port.insert(0, DEFAULT_PORT)
    port.place(x=165, y=50)

    nick = Entry(root)
    nick.place(x=165, y=80)

    auth = Entry(root)
    auth.insert(0, 'offline')
    auth.place(x=165, y=110)

    version = Entry(root)
    version.place(x=165, y=140)

    Label(root, text='IP Address: ', bg='#F0F8FF', font=('arial', 12)).place(x=35, y=20)
    Label(root, text=f'IP Port ({DEFAULT_PORT}): ', bg='#F0F8FF', font=('arial', 12)).place(x=35, y=50)
    Label(root, text='Username: ', bg='#F0F8FF', font=('arial', 12)).place(x=35, y=80)
    Label(root, text='Auth (offline/microsoft): ', bg='#F0F8FF', font=('arial', 10)).place(x=35, y=110)
    Label(root, text='Version (optional): ', bg='#F0F8FF', font=('arial', 12)).place(x=35, y=140)

    config = load_config('config.ini')

    start_button = Button(
        root,
        text='Start the bot',
        bg='#F0F8FF',
        font=('arial', 12),
        command=lambda: start_bot_thread(
            host.get().strip() or DEFAULT_HOST,
            port.get().strip() or DEFAULT_PORT,
            nick.get().strip(),
            config,
            auth.get().strip().lower() or 'offline',
            version.get().strip()
        )
    )
    start_button.place(x=242, y=173)

    Button(root, text='Server List', bg='#F0F8FF', font=('arial', 12), command=server_list).place(x=20, y=173)
    Button(root, text='Stop', bg='#F0F8FF', font=('arial', 12), command=stop_bot_thread).place(x=146, y=173)
    Button(root, text="Thanks to", bg="#F0F8FF", font=('arial', 12), command=open_thanks_to).place(x=20, y=210)
    Button(root, text="My GitHub Page", bg="#F0F8FF", font=('arial', 12), command=open_github_page).place(x=131, y=210)

    root.mainloop()


def server_list():
    """
    Displays the server list from ServerList.txt.
    """
    try:
        with open("ServerList.txt") as list_file:
            print(list_file.read())
    except FileNotFoundError:
        print("ServerList.txt not found.")


def open_thanks_to():
    """
    Opens the 'thanks to' link in the default web browser.
    """
    webbrowser.open('https://github.com/YTFort/24-Aternos')


def open_github_page():
    """
    Opens the GitHub page in the default web browser.
    """
    webbrowser.open('https://github.com/Ate329')


def cli_interface():
    """
    Provides a command-line interface for interacting with the bot.
    """
    config = load_config('config.ini')

    host = input(f"Enter IP Address (default {DEFAULT_HOST}): " ).strip() or DEFAULT_HOST
    port = input(f"Enter IP Port (default {DEFAULT_PORT}): " ).strip() or DEFAULT_PORT
    username = input("Enter Username: ")
    auth = input("Auth mode [offline/microsoft] (default offline): ").strip().lower() or 'offline'
    version = input("Minecraft version (optional, e.g. 1.20.4): ").strip()

    while True:
        print("1. Start the bot")
        print("2. Stop the bot")
        print("3. Show server list")
        print("4. Open based on link")
        print("5. Open GitHub page")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_bot_thread(host, port, username, config, auth, version)
        elif choice == '2':
            stop_bot_thread()
        elif choice == '3':
            server_list()
        elif choice == '4':
            open_thanks_to()
        elif choice == '5':
            open_github_page()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli_interface()
    else:
        create_ui()

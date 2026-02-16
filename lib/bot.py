from javascript import require
import platform
import os

bot = None
mineflayer = None


def _ensure_mineflayer():
    """Loads mineflayer only when needed to avoid failing at import time."""
    global mineflayer

    if mineflayer is not None:
        return mineflayer

    try:
        mineflayer = require('mineflayer')
    except Exception as err:
        raise RuntimeError(
            "Could not load 'mineflayer'. Install it with 'npm install mineflayer' "
            "and ensure npm registry access is available."
        ) from err

    return mineflayer


def create_bot(host, port, username, auth='offline', version=''):
    """Creates a new mineflayer bot instance."""
    global bot

    mineflayer_lib = _ensure_mineflayer()

    bot_options = {
        'host': host,
        'port': int(port) if str(port).strip() else 25565,
        'username': username,
        'auth': auth
    }

    if version:
        bot_options['version'] = version

    bot = mineflayer_lib.createBot(bot_options)
    return bot


def start_bot(host, port, username, config, handlers, auth='offline', version=''):
    """Starts the bot with given parameters and sets up handlers."""
    global bot
    bot = create_bot(host, port, username, auth, version)
    handlers.setup_handlers(bot, config)
    return bot


def stop_bot():
    """Stops the bot and terminates the node process based on the OS."""
    global bot

    if bot:
        bot.quit()
        bot = None

    current_os = platform.system()

    if current_os == "Windows":
        os.system('taskkill /f /im node.exe')
    elif current_os == "Linux":
        os.system('pkill -f node')
    else:
        print(f"Unsupported OS: {current_os}. Please terminate the Node.js process manually.")


if __name__ == "__main__":
    print("You are not suppose to run this module individually")

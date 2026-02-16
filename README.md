# MinecraftBot123
A minecraft bot with several functions eg. anti afk kick, raining detection, damage dection, welcome other players and also some basic chat event.

**Any pull requests are welcome.**

# Command (type in the minecraft chat)
Type ;pos in the server chat to show bot's coordinates.   
  
Type ;startafk to start anti afk kick.    
  
Type ;stopafk to stop.    
  
Type ;time ro check the current time in minecraft world.    

# Functions
Anti-afk    
    
Respond to simple messages    
    
Auto respawn    
    
Auto reconnecting to the servers    
    
Saying position   
    
Welcome and farewell players    
    
Game time checking    
    
Sending messages when players get damaged   
    
Sending messages about entity effetcs of players    
    
and so on......

# To-Do
This repository was created a long time ago but for some reasons it started being forked by people.  
Therefore, I guess I am going to start updating this repository if I have time.  

 - [ ] Allows the bot to follow a specific players and avoid obstacles.  


# Connecting to your own server
You can now configure the connection directly in both CLI and Tkinter modes:

- **IP Address**: your server host/domain
- **IP Port**: your server port (leave empty to use `57717`)
- **Username**: bot nickname
- **Auth**: `offline` for cracked servers, `microsoft` for premium accounts
- **Version (optional)**: set your Minecraft version (for example `1.20.4`) when auto-detect fails
- **Default Host**: `semcheats.aternos.me`
- **Aternos note**: your server must be started in Aternos panel before bot can connect

## CLI quick start
1. Run `python main.py`
2. Type `cli`
3. Fill in host/port/username/auth/version
4. Choose option `1` to start the bot

# Server List 
Go to ServerList.txt and add servers (cracked).

# Libraries
threading   
    
webbrowser    
    
configparser    
    
tkinter   
    
javascript    

## Special instructions for using devenv
You should run `npm install mineflayer` first to install required JavaScript dependencies.
JsPyBridge should have provided a workaround, but perhaps due to NixOS peculiarities it may not work.

# Thanks to
[Mineflayer](https://github.com/PrismarineJS/mineflayer)  
  
[YTFort/24-Aternos](https://github.com/YTFort/24-Aternos/)

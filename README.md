# Telegram-Translator-Channel-Bot

This is a python script to perform post extraction from a channel/group(foreign language) and translate to english before posting to a different group/channel on Telegram. To use the script, first

- Clone the repository to your local machine
    
        $ git clone https://github.com/Pycomet/Telegram-Translator-Channel-Bot.git
    
    After cloning the repository, move into cloned directory and install requirements
    
        pip install -r requirements.txt  (Windows Users)
        
    Or
    
        source my_env/bin/activate  (Linux Users)
        
    You can then go ahead to set the configuration in the TelegramBot.py. Change the following;
    
      - Api Id
      - Api Hash
      - Bot Token
      - Channel Id
      
Finally you can run the script

      python TelegramBot.py

# Discord Bot (ver 0.0.1)

### Necessary permissions
* Scopes
    * bot
    * applications.commands

* Bot Permissions
    * General Permissions
        * Read Messages/View Channels
    * Text Permissions
        * Send Messages
        * Manage Messages
        * Embed Links
        * Attach Files
        * Read Message History
        * Mention Everyone
        * Use External Stickers
        * Add Reactions
    * Voice Permissions
        * Connect
        * Speak

### Server Requirements to install
* Python: 3.11.2
* pip3: 22.3.1
* ffmpg
```sh
sudo apt install python3 python3-pip ffmpeg
```

### Packages to install
* discord                   2.2.2
* jproperties               2.1.1
* validators                0.20.0
* yt-dlp                    2023.2.17
* PyNaCl                    1.5.0
* pyinstaller               5.11.0
* pyinstaller-hooks-contrib 2023.3

### Install Packages
Command to install: 
```sh
pip3 install discord==2.2.2 jproperties==2.1.1 validators==0.20.0 yt-dlp==2023.2.17 pynacl==1.5.0 pyinstaller==5.11.0 pyinstaller-hooks-contrib==2023.3
```

#### Problems with youtube-dl
In case to have problems with this package, follow the next steps to install a stable version
```sh
pip3 uninstall yt-dlp
python3 -m pip install yt-dlp==2023.2.17
```

## Build executable
```sh
pyinstaller main.py --clean --onefile --name bot-<version>
chmod +x file_name
```

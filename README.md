# Discord Bot

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

### Python and pip version
* Python: 3.11.2
* pip3: 22.3.1

### Packages to install
* discord: 2.2.2
* jproperties: 2.1.1
* validators: 0.20.0
* youtube-dl: 2021.12.17
* PyNaCl: 1.5.0

#### Problems with youtube-dl
In case to have problems with this package, follow the next steps to install a stable version
```sh
pip3 uninstall yt-dlp
python3 -m pip install yt-dlp==2023.2.17
```

### Install Packages
Command to install: 
```sh
pip3 install discord jproperties validators youtube-dl pynacl
```
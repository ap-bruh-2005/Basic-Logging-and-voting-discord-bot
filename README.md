# Simple Discord logging and anonymous voting bot

This repository has code for basic logging and anonymous voting features for a discord bot.

## How to run the bot

First check if you have the required packages in requirements.txt. If you don't then install all the required packages. This can be done using pip.

After installation go to discord developer portal (The link is given below) and login to your account: https://discord.com/developers/docs/intro

When you are in the portal create a new Application and click on that application. Please allow all member intents.Then click on Bot under settings and copy the token. Paste that token in the tokens.txt file. When you want to run the bot, run the file main.py after pasting that token. Add the bot to all the server you want it in. 

At first add the guild id for the guild you need logging for in the guild.txt file. Add the role id for people who need access to the logging feature and anonymous voting feature(If its everyone then you should add the @everyone id) in role.txt . Also add the user id of the person who needs access for the anonymous voting file in the show_file_id.txt. Finally, change the timezone to your timezone in the code.

```python
#Change the timezone to your current timezone in line 18. For example
tz = "Asia/Kolkata"
```


## Usage and running the program

To run the program : 

```bash
cd <Path to the directory all the files are in> (for example : cd Desktop)
python main.py

```
Note that running main.py without the other txt files(except requirements.txt) will give you an error.

```
To use help do : !bot_help
```


## Contributing
Pull requests are more than welcome. 

## License
[MIT](https://choosealicense.com/licenses/mit/)

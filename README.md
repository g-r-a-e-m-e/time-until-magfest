# time-until-magfest
Discord bot to count down the time until MAGFest 2024!

## Usage
Using `!time-until` will tell you the time until MAGFest 2024! Hooray!

## FAQs
`Does it work?`
Sure.

`Is the code clean?`
Totally. There are definitely no hardcoded dates...

`Is it useful?`
Do you believe in life after love?

`Can I repurpose this for any other date?`
Sure! Just change the *definitely not hardcoded date* in the `time_until()` function in `main.py` to whatever date your heart desires.

## Installation
*Note: README largely comes from the Setup instructions from [RedKrieg's heimdallr bot](https://github.com/RedKrieg/heimdallr/tree/main)*

### Set up your bot
Follow the current instructions from Discord at https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro

### Clone repository
```
git clone <repo_url>
cd time-until-magfest
```

### Configure venv and install requirements
```
sudo apt -y install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Create token in python directory
```
cd python
nano -w token.json
```
- In `token.json` enter `{"DISCORD_TOKEN": "<your_token>"}`
- `CTRL-X` > Enter/Return > `Y`

### Run the bot
```
(venv) ~/time-until-magfest/python$ python main.py
```

### Test in Discord!
Once the bot is in your server, test it using `!time-until`.

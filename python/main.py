###
### This bot prints the number of days, hours, and minutes until MAGFest 2024!
###
### made by @g-r-a-e-m-e

# Boilerplate
import arrow
import discord
from discord.ext import commands
import json

### Helper functions ###
# Get the current time based on local time
def get_current_time():
    # Current time in UTC
    utc = arrow.utcnow()
    # Return local time
    nyc = utc.to('America/New_York')
    return nyc

def get_message(current_datetime, future_datetime):
    # Specify message
    message = future_datetime.humanize(current_datetime, 
                                   only_distance = True,
                                   granularity = ['day', 'hour', 'minute'])
    return message

# Get the token
with open('token.json') as f:
    token = json.load(f)['DISCORD_TOKEN']

# Create the client
bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

### Command(s) ###
@bot.hybrid_command(name = 'time-until')
async def time_until(command):
    # Get current time
    now = get_current_time()
    # Hardcode the f**k out of the MAGFest 2024 date
    magfest = arrow.get('2024-01-17 00:00:01 America/New_York', 'YYYY-MM-DD HH:mm:ss ZZZ')
    # Generate and return message
    message = f"There are {get_message(now, magfest)} until MAGFest 2024!"
    await command.send(message)

# Run!
bot.run(token)

###
### This bot prints the number of days, hours, and minutes until MAGFest 2024!
###
### made by @g-r-a-e-m-e

# Boilerplate
import arrow
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

### Helper functions ###
# Get the current time based on local time
def get_current_time():
    # Current time in UTC
    utc = arrow.utcnow()
    # Return local time
    return utc.to('local')

def get_message(current_datetime, future_datetime):
    # Specify message
    message = future_datetime.humanize(current_datetime, 
                                   only_distance = True,
                                   granularity = ['day', 'hour', 'minute'])
    return message

# Load .env file
load_dotenv()

# Get the token
token = os.getenv('DISCORD_TOKEN')

# Create the client
bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

### Command(s) ###
@bot.hybrid_command(name = 'time_until_magfest')
async def time_until(command):
    # Get current time
    now = get_current_time()
    # Hardcode the f**k out of the MAGFest 2024 date
    magfest = arrow.get('2024-01-24')
    # Generate and return message
    message = f"There are {get_message(now, magfest)} until MAGFest 2024!"
    await command.send(message)

# Run!
bot.run(token)

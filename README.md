# York University Timetable Avaliblity Checker

## Description
This is a simple discord bot scripted in python that checks the avaliblity of a course at York University for a defined faculty, subject, session, course code, and section. The bot will check the avaliblity of the course every defined interval of time and will update a database and notify members via ping in a discord channel alerting them of a change in avaliblity. Addtionally, the bot will keep track of the properties and avaliblility statistics for various courses and will display them in a discord channel upon user request.

## Setup
In order to set up the bot for your own use, the following steps must be taken:
### Set up .env file
1. Create a .env file in the root directory of the project
2. Add the following lines to the .env file:
```
# .env
DISCORD_TOKEN={your discord bot token}
YORK_USERNAME={your york username}
YORK_PASSWORD={your york password}
```
### Set up database
1. Create a database in the root directory of the project
2. Add the following lines to the database:
```

```
### Set up discord server
1. Create a discord server
2. Create a channel for the bot to post in
3. Create a role for the bot to ping
4. Create a channel for the bot to listen in
5. Use the following command to get the channel id of the channel for the bot to listen in:
```
\#channel
```
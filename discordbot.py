import os
import discord
import re
from dotenv import load_dotenv
from discord.ext import commands
import pickle


class Course:
    def __init__(self, Faculty, Subject, Session, CourseCode, Section):
        self.faculty = Faculty
        self.subject = Subject
        self.session = Session
        self.courseCode = CourseCode
        self.section = Section
        self.subscribers = []

    def subscribe(self, userID):
        self.subscribers.append(userID)

    def unsubscribe(self, userID):
        self.subscribers.remove(userID)


# loads the saved list of courses
def loadCourses():
    try:
        with open('courses.pickle', 'rb') as f:
            return pickle.load(f)
    except:
        return []


# saves the list of courses
def saveCourses(courses):
    with open('courses.pickle', 'wb') as f:
        pickle.dump(courses, f)


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


courses = loadCourses()


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    print("Message received by bot")
    if message.author == client.user:
        return

    if message.content.startswith('!lastAvailable'):
        # get the parameter after the command
        pattern = r'!lastAvailable\s+(.+)'
        match = re.search(pattern, message.content)

        # get the course code
        if match:
            courseCode = match.group(1)
            print(f"Course code: {courseCode}")

    if message.content.startswith('!hello'):
        await message.channel.send("Hello!")

    if message.content.startswith('!courseSub'):
        pattern = r'!courseSub\s+(.+)\s+(.+)'
        match = re.search(pattern, message.content)

        if match:
            course, section = match.group(1)
            user = message.author.id
            print(f"User: {user} added -> Course: {course} Section: {section}")

    # saves the list of courses
    saveCourses(courses)


client.run(token)

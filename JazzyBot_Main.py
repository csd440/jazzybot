#!/usr/bin/python
#Hide deprecated syntax warnings for ssl
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from flask import Flask
from flask import request
import requests
from Configurations import *
from JazzySkills import showusers,jazzySkills,createRoom,membership,getEmails

app = Flask(__name__)
underConstruction=('I am currently under construction, please check back later.  You may ask for help to see what I am trying to learn')
skillz=('I am a personal assistant bot and I am being programmed to do the following.\n')
#Routes
#Webhook should be created from CISCO Spark side and it should be directed to a specific address which can be accessible by the bot's backend
@app.route('/', methods=['POST'])
def get_tasks():
    messageId = request.json.get('data').get('id')
    messageDetails = requests.get(host+"messages/"+messageId, headers=headers)
    replyForMessages(messageDetails)
    return ""

#Functions
#A function to send the message by particular email or space
def sendMessage(message,  toRoom):
    payload = {'roomId': toRoom, 'text': message}
    response = requests.post(host+"messages", data=payload,  headers=headers)
    return response.status_code

#A function to get the reply and generate the response of from the bot's side
def replyForMessages(response):
    responseMessage = response.json().get('text')
    toRoom = response.json().get('roomId')
    toPersonEmail = response.json().get('personEmail')
    if toPersonEmail != botEmail:
        if 'help' in responseMessage:
            jSkills=jazzySkills()
            messageString = (skillz+' '+jSkills)
            sendMessage(messageString, toRoom)
        elif '/create' in responseMessage:
            newRoom=responseMessage.split('/create',1)[1].split('/')[0]
            messageString =('I will create a Spark Space called:\n'+newRoom)
            sendMessage(messageString, toRoom)
            createdRoom=createRoom(newRoom)
            messageString2= (newRoom,'has been created')
            roomId=createdRoom['id']
            sendMessage(messageString2, toPersonEmail)
            isModerator=True
            isNotModerator=False
            moderator=membership(roomId, toPersonEmail, isModerator)
            if '/add all' in responseMessage:
                users=getEmails(toRoom)
                for user in users:
                    roomMembers=membership(roomId, user, isNotModerator)
            if '/addemail' in responseMessage:
                emails=responseMessage.split('/addemail',1)[1].split('/')[0]
                emailList=emails.split(',')
                for user in emailList:
                    roomMembers=membership(roomId, user, isNotModerator)
        elif '/showusers' in responseMessage:
            messageString = 'Here is a list of users in this space\n'
            users=showusers(toRoom)
            sendMessage(messageString, toRoom)
            for user in users:
                sendMessage(user, toRoom)
        else:
            messageString = underConstruction
            sendMessage(messageString, toRoom)

if __name__ == "__main__":
    app.run(host=server, port=port, debug=False)
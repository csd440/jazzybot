###Skills of JazzyBot###
import requests
import json
from Configurations import *

def jazzySkills():
    printUsers=('I can print the users in this space:\n\t@JazzyBot /showusers')
    createRoom=('I can create a new Spark space:\n\t@JazzyBot /create <space_name>')
    addUsers=('I can create a new Spark space with users from this room:\n\t@JazzyBot /create <space_name> /add all')
    addEmails=('I can create a new Spark space with your own email list:\n\t@JazzyBot /create <space_name> /addemail <bob@em.com,cat@em.com> "comma seperated emails"')
    killDogs=('I am being programmed to kill annoying dogs that wake you early in the morning')
    zhelp=('I can display my skills by issueing help:\n\t@JazzyBot /help')
    jazzySkillz=(printUsers+'\n'+createRoom+'\n'+addUsers+'\n'+addEmails+'\n'+killDogs+'\n'+zhelp+'\n')
    return jazzySkillz

def showusers(toRoom):
    userList=[]
    params={'roomId':toRoom}
    response=requests.get(host+'memberships',params=params,headers=headers)
    apiResponse=json.loads(response.text)
    for id in apiResponse['items']:
        userList.append(id['personDisplayName'])
    return userList

def getEmails(toRoom):
    emailList=[]
    params={'roomId':toRoom}
    response=requests.get(host+'memberships',params=params,headers=headers)
    apiResponse=json.loads(response.text)
    for id in apiResponse['items']:
        emailList.append(id['personEmail'])
    return emailList

def createRoom(newRoom):
    params={'title':newRoom}
    response=requests.request('POST',host+'rooms',data=params,headers=headers)
    apiResponse=json.loads(response.text)
    return apiResponse

def membership (roomId,user,isModerator):
    params={'roomId':roomId,'personEmail':user,'isModerator':isModerator}
    response=requests.request('POST',host+'memberships',data=params,headers=headers)
    apiResponse=json.loads(response.text)
    return apiResponse

### This Web Hook is for Jazzy Bot ###
import requests
import json
ACCESS_TOKEN='YTVkN2RmNDYtMmExOS00OTBhLWE5MDQtZTU3Yjc0OTgwMjkwMzdmMjc0ZDAtNmE3'
webHookId='Y2lzY29zcGFyazovL3VzL1dFQkhPT0svMTUyYTFiODktMTE0Yi00OGFjLWJkMjctZWU1NWJkNTEzNTY5'
apiUrl=('https://api.ciscospark.com/v1/webhooks/'+webHookId)
headers={'Content-type':'application/json; charset=utf-8','Authorization':'Bearer '+ACCESS_TOKEN}
PARAMS={'name':'Jazzy Web Hook','targetUrl':'https://71b7d385.ngrok.io'}
response=requests.request('PUT',url=apiUrl,data=json.dumps(PARAMS),headers=headers)
apiResponse=json.loads(response.text)
print(apiResponse)

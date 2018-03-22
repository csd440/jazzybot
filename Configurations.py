#Modify botEmail and accessToken when creating new bot accounts
#Access token can be generated using the CISCO BOT account and Bot Email also can find in there
botEmail = "JazzyBot@sparkbot.io"#bot's email address
accessToken = "Enter Bot Token"#Bot's access token
host = "https://api.ciscospark.com/v1/"#end point which provides by the CISCO Spark to communicate between their services
server = "localhost"#Web hook won't work until the server sets up
port = 8443
headers = {'Authorization':'Bearer '+accessToken}
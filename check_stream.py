import requests

confirmArray = []
def check_stream():
    global confirmArray
    channelName = 'vedal987'
    response =  requests.get('https://www.twitch.tv/' + channelName)
    contents = response.content.decode('utf-8')
    if 'isLiveBroadcast' in contents:
        confirmArray = []
        return True
    elif str(response) == '<Response [200]>':
        confirmArray.append(response)
        if len(confirmArray) >= 10:
            return False
        else:
            return None

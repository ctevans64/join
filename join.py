import requests
class JoinInstance:

    def __init__(self, apikey, deviceid):
        self.deviceid = deviceid
        self.apikey = apikey
        self.url_root = f"https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?deviceId={self.deviceid}&apikey={self.apikey}"

    def sendNotification(self, title, text, icon=""):
        request_url = self.url_root + "&title=" + title + "&text=" + text
        if len(icon) > 0:
            request_url = request_url + "&icon=" + icon
        requests.get(url=request_url)

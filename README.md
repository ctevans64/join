# JOIN
A simple Join API wrapper for python. Create a JoinInstance with deviceid and apikey to access that devices Join API.

# Code example
```python
from join import JoinInstance
# Set up join
apikey = "JOIN API KEY"
deviceid = "JOIN DEVCICE ID"

join = JoinInstance(apikey=apikey, deviceid=deviceid)
# Create payload
title = "Notification title"
text = "This is the notification text"

print("Sending notification...")
join.sendNotification(title=title, text=text)
```
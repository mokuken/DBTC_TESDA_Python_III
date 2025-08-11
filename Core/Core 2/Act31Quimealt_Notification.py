# class Notification:
#     def send():
#         pass
    
# class EmailNotification(Notification):
#     def send():
#         print("Email sent.")

# class PushNotification(Notification):
#     def push_message():
#         print("Message pushed to other phone")

# class OfflineNotification(Notification):
#     def send():
#         raise Exception("it cannot send messages instantly and instead logs the message for later.")
    

# Your Task
# 1. Which programming principle is broken here?
# Ans: it breaks the Liskov Substitute Principle here

# 2. Why does this cause a problem in the system?
# Ans: the  the base class (OfflineNotification) becasue expects the emails sends immediately

# 3. How would you change the design so all notifications work correctly without breaking the program
# Ans: im ganno create a two new child class that will become a parent class of ther sub classes

class Notification:
    def send(self, message):
        pass


class ImmediatelySend(Notification):
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.send(message)


class DelayedSend(Notification):
    def __init__(self, notification):
        self.notification = notification

    def log_for_later(self, message):
        self.notification.log_for_later(message)


class EmailNotification:
    def send(self, message):
        print("Email sent:", message)


class PushNotification:
    def send(self, message):
        print("Push sent:", message)


class OfflineNotification:
    def log_for_later(self, message):
        print("Offline sent:", message)


# Usage
email = ImmediatelySend(EmailNotification())
push = ImmediatelySend(PushNotification())
offline = DelayedSend(OfflineNotification())

email.send("Sent via email")
push.send("Sent via push")
offline.log_for_later("Sent via offline")

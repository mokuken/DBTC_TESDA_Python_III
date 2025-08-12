class MessagingApp:
    def send_message(self, message):
        pass

class VideoCallApp:
    def start_call(self, person):
        pass

class SocialMediaApp(MessagingApp, VideoCallApp):
    def send_message(self, message):
        print("Message Sent:", message)

    def start_call(self, person):
        print("Calling:", person)


class ChatOnlyApp(MessagingApp):
    def send_message(self, message):
        print("Message Sent:", message)


# Calling the SocialMediaApp Methods
messager = SocialMediaApp()
messager.send_message("Hello, World!")
messager.start_call("my mother")

# Calling the ChatOnlyApp Methods
chat = ChatOnlyApp()
chat.send_message("Hello, Friend!")
Python
import time
import random

class MiniChatbotNotifier:
    def __init__(self, username):
        self.username = username
        self.notifications = []

    def notify(self, message):
        self.notifications.append(message)
        print(f"Notifying {self.username}: {message}")

    def check_notifications(self):
        if self.notifications:
            print(f"{self.username} has {len(self.notifications)} new notifications:")
            for notification in self.notifications:
                print(f"- {notification}")
            self.notifications = []
        else:
            print(f"No new notifications for {self.username}")

def test_minichatbot_notifier():
    notifier = MiniChatbotNotifier("M0VV")
    notifier.notify("You have a new message from John!")
    notifier.notify("You have a new message from Jane!")
    notifier.check_notifications()
    time.sleep(2)  # simulate some time passing
    notifier.notify("You have a new message from Bob!")
    notifier.check_notifications()

test_minichatbot_notifier()
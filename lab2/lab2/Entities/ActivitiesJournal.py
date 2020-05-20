import json
from Entities.Storage import Storage


class Journal:
    logging = None
    storage = None
    pubsub = None

    def __init__(self, logger=True):
        self.storage = Storage()
        self.pubsub = self.storage.connection.pubsub()
        self.logging = logger
        self.pubsub.subscribe('ActivitiesJournal')
        print('Journal created\nAll activities will be displayed here')

    def start(self):
        while True:
            pubsub_message = self.pubsub.get_message()
            if pubsub_message and pubsub_message['type'] == 'message':
                message = json.loads(pubsub_message['data'])
                message_type = message['type']
                if message_type == 'spam':
                    self.add_spammer(message['sender'])
                    if self.logging:
                        print("User {} tried to send spam to {}".format(message['sender'], message['receiver']))
                if message_type == 'connected':
                    self.user_connected()
                    if self.logging:
                        print('User {} just connected!'.format(message['user']))
                if message_type == 'disconnected':
                    self.user_disconnected()
                    if self.logging:
                        print('User {} disconnected!'.format(message['user']))

    def user_connected(self):
        return self.storage.increment_online_count()

    def user_disconnected(self):
        return self.storage.decrement_online_count()

    def add_spammer(self, username):
        self.storage.increment_spam_count(username)

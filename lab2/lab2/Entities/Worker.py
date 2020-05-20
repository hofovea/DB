import os
import random
import json
from time import sleep
from Entities.Storage import Storage
from Entities.Status import Status


class Worker:
    spam_ratio = 0.5
    working = False
    storage = None

    def __init__(self):
        self.storage = Storage()
        print('Workker created with PID: ' + os.getpid().__repr__())

    def is_spam(self):
        sleep(random.random() * 5)
        return (random.choices([True, False], [self.spam_ratio, 1 - self.spam_ratio], k=1))[0]

    def start_check(self):
        while True:
            hashcode = self.storage.get_message_hashcode_from_queue()
            if hashcode:
                self.storage.update_message_status(hashcode, Status.CHECK)
                message = self.storage.get_message(hashcode)
                print('Message from ' + message['Sender'] + ' with status ' + message['Status'])
                if self.is_spam():
                    print(message['Sender'] + ' sent spam!')
                    self.storage.connection.publish('ActivitiesJournal',
                                                    json.dumps({'type': 'spam', 'sender': message['Sender'],
                                                                'receiver': message['Receiver']}))
                    self.storage.update_message_status(hashcode, Status.SPAM)
                else:
                    receiver = self.storage.get_message_receiver(hashcode)
                    self.storage.update_message_status(hashcode, Status.SENT)
                    self.storage.send_message(hashcode, receiver)
                    print("Message from {} was checked and sent".format(message['Sender']))

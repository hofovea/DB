from Entities.Client import Client
from PyInquirer import prompt
from UI import menu_variation


class UI:
    client = Client()
    menu_type = None

    def __init__(self, client_name):
        self.client.username = client_name
        if self.client.is_admin(client_name):
            self.menu_type = menu_variation.admin_ui
        elif self.client.is_owner(client_name):
            self.menu_type = menu_variation.owner_ui
        elif self.client.is_common_user(client_name):
            self.menu_type = menu_variation.common_ui

    def start(self):
        while True:
            op = prompt(self.menu_type)['operation']
            if op == 'New message':
                message = prompt(menu_variation.input_message)['value']
                receiver = prompt(menu_variation.input_username)['value']
                if self.client.is_exists(receiver):
                    self.client.create_message(message, receiver)
                else:
                    print('Can`t send message to {}: user does not exist'.format(receiver))
            if op == 'Inbox':
                messages = self.client.get_inbox(self.client.username, 10)
                if messages:
                    message_list = []
                    for hashcode in messages:
                        mess = self.client.get_message(hashcode)
                        message_dict = {'message_str': mess['Sender'] + ' ' + mess['Message'][:8] + '...',
                                        'hashcode': hashcode}
                        message_list.append(message_dict)
                    hashcode_new = prompt(menu_variation.choose_message(message_list))['value']
                    print(self.client.get_message(hashcode_new)['Message'])
                    self.client.storage_manager.update_message_status(hashcode_new, 'RECEIVED')
                else:
                    print('No messages')
            if op == 'View rating of spammers':
                spammers = self.client.get_spammers(10)
                for spammer in spammers:
                    print(spammer[0] + ': {} '.format(int(spammer[1])) + 'spam messages')
            if op == 'View Online':
                print(self.client.get_online())
            if op == 'Promote to admin':
                username = prompt(menu_variation.input_username)['value']
                if self.client.is_admin(username) or self.client.is_owner(username):
                    print("User {} is already admin".format(username))
                else:
                    self.client.promote_to_admin(username)
            if op == 'Demote to user':
                username = prompt(menu_variation.input_username)['value']
                if self.client.is_common_user(username):
                    print("User {} is already common user".format(username))
                else:
                    self.client.demote_to_user(username)
            if op == 'Quit':
                self.client.disconnect()
                quit()

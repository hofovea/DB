import sys
from Entities.Client import Client
from PyInquirer import prompt
from UI import menu_variation
from UI.UI import UI

client = Client()
username = prompt(menu_variation.input_name)['value']
if client.is_exists(username):
    client.connect(username)
else:
    if len(sys.argv) > 1 and sys.argv[1] == 'owner':
        client.add_owner(username)
    elif len(sys.argv) > 1 and sys.argv[1] == 'admin':
        client.add_admin(username)
    else:
        client.add_user(username)
    client.connect(username)

ui = UI(username)
ui.start()

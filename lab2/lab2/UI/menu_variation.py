# interfaces for promt
common_ui = [
    {
        'type': 'list',
        'message': 'Select operation',
        'name': 'operation',
        'choices': [
            {
                'name': 'New message'
            },
            {
                'name': 'Inbox'
            },
            {
                'name': 'Quit'
            }
        ]
    }
]

admin_ui = [
    {
        'type': 'list',
        'message': 'Select operation',
        'name': 'operation',
        'choices': [
            {
                'name': 'New message'
            },
            {
                'name': 'Inbox'
            },
            {
                'name': 'View Online'
            },
            {
                'name': 'View rating of spammers'
            },
            {
                'name': 'Quit'
            }
        ]
    }
]

owner_ui = [
    {
        'type': 'list',
        'message': 'Select operation',
        'name': 'operation',
        'choices': [
            {
                'name': 'New message'
            },
            {
                'name': 'Inbox'
            },
            {
                'name': 'View Online'
            },
            {
                'name': 'Promote to admin'
            },
            {
                'name': 'Demote to user'
            },
            {
                'name': 'View rating of spammers'
            },
            {
                'name': 'Quit'
            }
        ]
    }
]

input_name = [{
    'type': 'input',
    'name': 'value',
    'message': 'Enter the name'
}]

input_message = [{
    'type': 'input',
    'name': 'value',
    'message': 'Enter the message'
}]

input_username = [{
    'type': 'input',
    'name': 'value',
    'message': 'Enter the Username'
}]


def choose_message(messages):
    choice_message = [
        {
            'type': 'list',
            'name': 'value',
            'message': 'Choose message to view',
            'choices': []
        }
    ]
    for message in messages:
        obj = {
            'value': message['hashcode'],
            'name': message['message_str']
        }
        choice_message[0]['choices'].append(obj)
    return choice_message

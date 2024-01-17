import json

with open('commands.json', 'r') as f:
    data = json.load(f)

new_data = []
new_command = {}

# ToDo - insert weight values into json
for command in data:
    if command['chapter'] != "" and 'Note' not in command:
        if new_command != {}:
            new_data.append(new_command)
        new_command = {
            'chapter': command['chapter'],
            'description': command['description'],
            'command': command['command'],
            'script': command.get('script', ''),
            'level': command['level'],
            'weight': 0
        }

        if new_command['level'] == 1:
            new_command['level'] = [1, 1]
        elif new_command['level'] == 2:
            new_command['level'] = [2, 2]
        elif new_command['level'] == 12:
            new_command['level'] = [1, 2]

    elif command['chapter'] == "" and not 'Note' in command:
        if new_command != {}:
            new_command['command'] += '; ' + command['command']
    elif command['chapter'] == "" and 'Note' in command:
        new_command = {}
    elif command['chapter'] != "" and 'Note' in command:
        if new_command != {}:
            new_data.append(new_command)
            new_command = {}

with open('own_commands.json', 'w') as f:
    json.dump(new_data, f, indent=4)

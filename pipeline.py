### -------------- Pipline distro information --------------------
version = '0.0.2'
com = []    # the command will be in a list so that I can clearify if it was given by the user or by the terminal.
            # this is to prevent the terminal from talking to itsel. This will become clear in future cases.

### -------------- All the lists required to fuel the terminal --------------------
commands = [
    '\n----- Informational commands ----------'
    ,'help (will print a list of commands that you can use.'
    ,'stop, quit, break, shutdown, end (will stop the pipeline)'
    
    ,'\n----- Fun and interesting commands ----'
    ,'hi, hello'
]
rloffc = [ ## raw_lst_off_commands
    'help', 'stop', 'quit', 'break', 'shutdown', 'end', 'hi', 'hello',
]

### -------------- All the definitions needed to keep the engine running
def print_lst_one_by_one(lstname: list, way: str) -> str:
    if way == 'with_enters':
        for lstelement in range(len(lstname)):
            print(lstname[lstelement])
    if way == 'with_tabs':
        for lstelement in range(len(lstname)):
            try:
                if len(lstname[lstelement]) < 15 and len(lstname[lstelement + 1]) < 15 and len(lstname[lstelement + 2]) < 15 and len(lstname[lstelement + 3]) < 15:
                    print(lstname[lstelement], '\t\t', lstname[lstelement + 1], '\t\t', lstname[lstelement + 2], '\t\t', lstname[lstelement + 3])
                else:
                    print(lstname[lstelement], '\t\t\t', lstname[lstelement + 1], '\t\t\t', lstname[lstelement + 2], '\t\t\t', lstname[lstelement + 3])
            except IndexError:
                break
    if way == 'no_style':
        for lstelement in range(len(lstname)):
            print(lstname[lstelement])
    return '\n'

### -------------- Start and beforahand setting -------------------
skip_initial_command = False
commanding = True
while commanding is True: ## This while loop will keep the converstation going.
    if skip_initial_command is False:
        newcom = input('>>> ')
        com.append(newcom)
        com.append('freedom') ## This will verify that the command was given by the user and not the terminal.
    skip_initial_command = False

### -------------- All the commands -------------------------------
    if 'stop' in com or 'quit' in com or 'break' in com or 'shutdown' in com or 'end' in com:
        break
    if 'hi' in com or 'hello' in com and com[-1] == 'freedom':
        print('\nHello there what can I help you with?')
    if 'help' in com and com[-1] == 'freedom':
        print('\nThese are the commands you can use in the pipeline terminal.')
        print_lst_one_by_one(commands, 'with_enters')

### -------------- Guessing work if typo occurs --------------------
    if len(com) == 2:
        command = com[0]    ## transforms the command from a list back too a string.
    else:                   ## as of now the length of comm will always be 2 this might change in the future.
        for i in range(len(com) - 1): 
            seperator = ' '
            command = seperator.join(com)
    if command not in rloffc and com[-1] == 'freedom':
        for gues_command in rloffc:
            current_command_check = []
            count = 0
            for kar in gues_command :
                current_command_check.append(kar)
            for kar in command:
                if kar in current_command_check:
                    count += 1
            count = float(count)
            count_down = 0.90
            if count >= count_down * len(com):
                print('Did you mean to type:', gues_command, '?')
                answer = input('yes, no, stop: ')
                if answer == 'yes':
                    com[0] = gues_command
                    skip_initial_command = True
                    break
                if answer == 'stop' or answer == 'quit':
                    break
            count_down -= 0.05
        if answer != 'stop' and  answer != 'yes' and  answer != 'quit':
            print("Sorry I didn't get that, try typing the command again. \nOr use the command help for more info.")
            com.clear() ## clears the list that was created for the current command. So that the new command
                        ## can be taken in.
#-------------------#-------------------Kill
print('Bye see you next time.')
quit
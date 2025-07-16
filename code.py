#command-line to-do list application
tdlist=[{'task':'dummy', 'done':False}]
print('''hello this is your to do list. 
      what you can do is type
      \'add\', 
      \'del\', 
      \'list\', 
      \'done\' or 
      \'exit\' 
      to modify your great to do list. 
      let's go :)''')

while True: 
    usercommand = input('pls input your request:').strip().lower()
    if usercommand == 'add':
        task = input('please add a thing you want to do:')
        tdlist.append({'task': task, 'done': False})
        print(f'[SUCCESS] TASK {task} ADDED')
        #print(tdlist[1])

    elif usercommand == 'del':
        idx = int(input('pls enter the task index to delete the task from the to do list:'))
        if idx == 0:
            print('please enter a valid index')
        elif idx > len(tdlist)-1:
            print(f'you only have {len(tdlist)-1} items on the list, please try again.')
        else:
            deleted = tdlist.pop(idx)
            print(f'[SUCCESS] TASK {deleted['task']} DELETED')

    elif usercommand == 'list':
            if not tdlist:
                print('youve got nothing on the list mate')
            else:
                print('this is your todo list')
                for i, adict_in_list in enumerate(tdlist):
                    if adict_in_list['done'] == True:
                        statu = '1'
                    else:
                        statu = '[ ]'
                print(f"{i}: {statu} {adict_in_list.get('task')}")      
            print('hahahahahahahaha')


    elif usercommand == 'done':
        idx_done = int(input('input the index of the thing youve done:'))
        if idx_done == 0:
            print('please enter a valid index')
        elif idx_done > len(tdlist) - 1:
            print(f'you only have {len(tdlist)-1} items on the list, please try again.')
        else:
            tdlist[idx_done]['done'] = True
            print('well done!')

    else:
        print('try again, invalid cmd')

#if usercommand == 'exit':
#唔識
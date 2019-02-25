def print_list(plist):
    """
    This function print a list.
    """
    for item in plist:
        print(item)

def in_the_list(item, list1):
    """
    Verify if a name is in the list.
    """
    for i in list1:
        if item == i:
            return True
    return False

list1 = ['Alice', 'Giovani', 'Paulo', 'Grazzi']

keep_run = 'Y'
while keep_run == 'Y':
     name = input('Type the name: ')

     if in_the_list(name, list1):
         print('The name', name, 'is registered!')
     else:
         list1.append(name)

     keep_run = input('Want to insert another name? Yes (Y) No (any key).')

print_list(list1)

def removeDuplicate(fileName):
    try:
        print('Removing duplicate urls\n')
        file = open(fileName, 'r')
        allLinks = []
        
        for line in file.readlines():
            allLinks.append(line)
        
        newLinks = list(dict.fromkeys(allLinks))
        
        file2 = open('newLinks.txt', 'w')
        file2.writelines(newLinks)
        file2.flush()
        file2.close()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(f'Exception Ocurred, {message}\n')
    finally:
        print('Duplicates have been removed :) \n')
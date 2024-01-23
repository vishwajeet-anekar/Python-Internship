def readfile(filepath):
    try:
        with open(filepath,'r') as f:
            read = f.read()
            return read
    except ValueError as e:
        print('error occured due to name') 
    except IOError as i:
        print('File does not exist')
    else:
        print('No exception in this block')
    finally:
        print('file operation completed')
path = 'demo.txt'
ans = readfile(path)
print(ans)
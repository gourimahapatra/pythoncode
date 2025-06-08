try:
    x = 9
    print(x)
    print(y)
except NameError:
    print("Variable not found")
except:
    print("An Exception occured")
else:
    print("everything looks good")
finally:
    print("clear everyhing used here")


try:
    f = open("file.txt")
    try:
        f.write("dsfsdf")
    except:
        print("Something went wrong")
    finally:
        f.close()
except:
    print("Something wrong")
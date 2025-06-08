def httperror(status):
    match status:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print ("No able find")
        case _:
            print("something wrong")

httperror(400)
    
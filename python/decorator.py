def announce(f):
    def wrapper():
        print("About to run")
        f()
        print("Done running")
    return wrapper
        
@announce
def morning():
    print("Good Morning!")
    
morning()
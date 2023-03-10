def wrap (func) :
    
    def wrapping () :
        
        print("1")
        
        func()
        
        print("3")
    
    return wrapping

@wrap
def f():
    print("2")
    
f()
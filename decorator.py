def wrap (func , func2) :
    
    def wrapping () :
        
        print("1")
        
        func()
        
        print("4")
    
    return wrapping

@wrap

def f():
    print("2")
    
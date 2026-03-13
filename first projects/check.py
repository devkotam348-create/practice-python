class parent:
    def __init__(self):
        print("parent contructor")
    
class child(parent):
    def __init__(self):
        super().__init__()
        # print("child constructor")
        
e = child()
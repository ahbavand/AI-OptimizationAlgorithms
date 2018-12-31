class node:
    def __init__(self,state,parrent,cost):
        self.state=state
        self.parrent=parrent
        self.cost=cost



    def get_depth(self):
        if(self.parrent==None):
            return 0
        else:
            return (self.parrent.get_depth()+1)
from src.interfaces.i_auth import IAuth


class UCCarregarChave():

    auth : IAuth
    
    def __init__(self, auth : IAuth):
        self.auth = auth
        
    def __call__(self):
        return self.auth.carregarChave()

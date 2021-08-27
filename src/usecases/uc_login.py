from src.interfaces.i_armazenamento_auth import IArmazenamento
from devmaua.src.models.ra import RA

class UCLogin():
    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def logarComRa(self, ra: RA, senha, str):
        if self.usuariosRepo.raExiste(ra):

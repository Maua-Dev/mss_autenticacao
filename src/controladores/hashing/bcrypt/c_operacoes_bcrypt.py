from src.interfaces.i_operacoes_hash import IOperacoesHash
import bcrypt


#TODO Considerar tirar de Controladores e colocar em outro lugar
class COperacoesBcrypt(IOperacoesHash):

    def checarHashSenha(senha: str, hash: str) -> bytes:
        return bcrypt.checkpw(senha.encode(), hash.encode())

    def criarHashSenha(senha: str) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode(), salt)

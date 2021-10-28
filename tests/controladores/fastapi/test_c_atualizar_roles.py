import pytest
from devmaua.src.enum.roles import Roles
from fastapi import HTTPException

from src.controladores.fastapi.c_atualizar_roles import CAtualizarRolesFastApi
from src.models.login import Login
from unittest.mock import Mock, patch

from src.usecases.uc_usuario_auth import UCUsuarioAuth
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.models.erros.erros_models import ErroConversaoStrRole
from src.usecases.erros.erros_uc import ErroInesperado


class TestCAtualizarRoles:

    def criaBody(self):
        return {
            "email":"mail@mail.com",
            "roles":["ALUNO", "PROFESSOR"]
        }


    def criaRoles(self):
        return [Roles.ALUNO, Roles.PROFESSOR]

    @patch.object(Login, 'rolesFromStrList')
    @patch.object(UCUsuarioAuth, 'atualizarRoles')
    def testRespostaOK(self, mockAtualizar, mockLogin):

        mockLogin.return_value = self.criaRoles()

        c = CAtualizarRolesFastApi(Mock())(self.criaBody())

        assert c.body.decode() == "Atualizado com sucesso"
        assert c.status_code == 200

        #Verificar se da para chamar assert sem o "roles=" de outra forma...
        mockLogin.assert_called_once_with(roles=self.criaBody()["roles"])
        mockAtualizar.assert_called_once_with(email=self.criaBody()["email"], roles=self.criaRoles())

    @patch.object(Login, 'rolesFromStrList')
    @patch.object(UCUsuarioAuth, 'atualizarRoles')
    def testRespostaErroEmailNaoEncontrado(self, mockAtualizar, mockLogin):
        mockLogin.return_value = self.criaRoles()
        mockAtualizar.side_effect = ErroEmailNaoEncontrado()

        with pytest.raises(HTTPException) as e:
            CAtualizarRolesFastApi(Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailNaoEncontrado())
        assert exc.status_code == 404

        mockLogin.assert_called_once_with(roles=self.criaBody()["roles"])
        mockAtualizar.assert_called_once_with(email=self.criaBody()["email"], roles=self.criaRoles())

    @patch.object(Login, 'rolesFromStrList')
    @patch.object(UCUsuarioAuth, 'atualizarRoles')
    def testRespostaErroConversaoStrRole(self, mockAtualizar, mockLogin):
        mockLogin.side_effect = ErroConversaoStrRole()

        with pytest.raises(HTTPException) as e:
            CAtualizarRolesFastApi(Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroConversaoStrRole())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(roles=self.criaBody()["roles"])
        mockAtualizar.not_called()

    @patch.object(Login, 'rolesFromStrList')
    @patch.object(UCUsuarioAuth, 'atualizarRoles')
    def testRespostaErroInesperado(self, mockAtualizar, mockLogin):
        mockLogin.return_value = self.criaRoles()
        mockAtualizar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CAtualizarRolesFastApi(Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroInesperado())
        assert exc.status_code == 500

        mockLogin.assert_called_once_with(roles=self.criaBody()["roles"])
        mockAtualizar.assert_called_once_with(email=self.criaBody()["email"], roles=self.criaRoles())

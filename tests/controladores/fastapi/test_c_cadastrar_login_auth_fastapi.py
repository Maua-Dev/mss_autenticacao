import pytest
from unittest.mock import Mock, patch
from fastapi import HTTPException

from src.controladores.fastapi.c_cadastrar_login_auth_fastapi import CCadastrarLoginAuthFastApi
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin
from src.usecases.erros.erros_uc import ErroEmailJaCadastrado, ErroInesperado
from src.models.login import Login

from src.usecases.uc_usuario_auth import UCUsuarioAuth
from tests import mock_objetos


class TestCCadastrarLoginAuthFastApi:

    def criaBody(self):
        return {
            "email":"mail@mail.com",
            "senha":"senha"
        }

    @patch.object(Login, 'fromDict')
    @patch.object(UCUsuarioAuth, 'cadastrarLoginAuth')
    def testRespostaOK(self, mockCadastrar, mockLogin):

        mockLogin.return_value = mock_objetos.mockLogin()

        c = CCadastrarLoginAuthFastApi(Mock(), Mock())(self.criaBody())

        assert c.body.decode() == "Cadastrado com sucesso"
        assert c.status_code == 201

        mockLogin.assert_called_once_with(self.criaBody())
        mockCadastrar.assert_called_once_with(mock_objetos.mockLogin())

    @patch.object(Login, 'fromDict')
    @patch.object(UCUsuarioAuth, 'cadastrarLoginAuth')
    def testRespostaComErroEmailVazio(self, mockCadastrar, mockLogin):

        mockLogin.side_effect = ErroEmailVazio()

        with pytest.raises(HTTPException) as e:
            CCadastrarLoginAuthFastApi(Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailVazio())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockCadastrar.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCUsuarioAuth, 'cadastrarLoginAuth')
    def testRespostaComErroEmailInvalido(self, mockCadastrar, mockLogin):

        mockLogin.side_effect = ErroEmailInvalido()

        with pytest.raises(HTTPException) as e:
            CCadastrarLoginAuthFastApi(Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailInvalido())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockCadastrar.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCUsuarioAuth, 'cadastrarLoginAuth')
    def testRespostaComErroSenhaVazio(self, mockCadastrar, mockLogin):

        mockLogin.side_effect = ErroSenhaVazio()

        with pytest.raises(HTTPException) as e:
            CCadastrarLoginAuthFastApi(Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroSenhaVazio())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockCadastrar.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCUsuarioAuth, 'cadastrarLoginAuth')
    def testRespostaComErroConversaoRequestLogin(self, mockCadastrar, mockLogin):

        mockLogin.side_effect = ErroConversaoRequestLogin()

        with pytest.raises(HTTPException) as e:
            CCadastrarLoginAuthFastApi(Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroConversaoRequestLogin())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockCadastrar.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCUsuarioAuth, 'cadastrarLoginAuth')
    def testRespostaComErroEmailJaCadastrado(self, mockCadastrar, mockLogin):

        mockLogin.return_value = mock_objetos.mockLogin()
        mockCadastrar.side_effect = ErroEmailJaCadastrado()

        with pytest.raises(HTTPException) as e:
            CCadastrarLoginAuthFastApi(Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailJaCadastrado())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockCadastrar.assert_called_once_with(mock_objetos.mockLogin())

    @patch.object(Login, 'fromDict')
    @patch.object(UCUsuarioAuth, 'cadastrarLoginAuth')
    def testRespostaComErroInesperado(self, mockCadastrar, mockLogin):

        mockLogin.return_value = mock_objetos.mockLogin()
        mockCadastrar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CCadastrarLoginAuthFastApi(Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroInesperado())
        assert exc.status_code == 500

        mockLogin.assert_called_once_with(self.criaBody())
        mockCadastrar.assert_called_once_with(mock_objetos.mockLogin())

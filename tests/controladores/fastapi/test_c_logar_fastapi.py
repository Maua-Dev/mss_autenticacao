import pytest
from unittest.mock import Mock, patch
from fastapi import HTTPException

from src.controladores.fastapi.c_logar_fastapi import CLogarFastApi
from src.models.login import Login
from src.usecases.uc_criar_token import UCCriarToken
from src.usecases.uc_login import UCLogin
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin
from src.usecases.erros.erros_uc import ErroEmailEOuSenhaIncorretos, ErroInesperado
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado



class TestCLogarFastapi:

    def criaBody(self):
        return {
            "email":"mail@mail.com",
            "senha":"senha"
        }

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testRespostaOK(self, mockCriarToken, mockAutenticar, mockLogin):
        mockAutenticar.return_value = True
        mockCriarToken.return_value = "token"

        c = CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        assert c.body.decode() == "token"
        assert c.status_code == 200

        mockLogin.assert_called_once_with(self.criaBody())
        mockAutenticar.assert_called_once_with(mockLogin.return_value)
        mockCriarToken.assert_called_once()


#TODO considerar usar @parametrized ou algo do tipo para nao repetir codigo -> igual para td erro

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testErroEmailVazio(self, mockCriarToken, mockAutenticar, mockLogin):

        mockLogin.side_effect = ErroEmailVazio()

        with pytest.raises(HTTPException) as e:
            CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailVazio())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockAutenticar.assert_not_called()
        mockCriarToken.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testErroEmailInvalido(self, mockCriarToken, mockAutenticar, mockLogin):

        mockLogin.side_effect = ErroEmailInvalido()

        with pytest.raises(HTTPException) as e:
            CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailInvalido())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockAutenticar.assert_not_called()
        mockCriarToken.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testErroSenhaVazio(self, mockCriarToken, mockAutenticar, mockLogin):

        mockLogin.side_effect = ErroSenhaVazio()

        with pytest.raises(HTTPException) as e:
            CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroSenhaVazio())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockAutenticar.assert_not_called()
        mockCriarToken.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testErroConversaoRequestLogin(self, mockCriarToken, mockAutenticar, mockLogin):

        mockLogin.side_effect = ErroConversaoRequestLogin()

        with pytest.raises(HTTPException) as e:
            CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroConversaoRequestLogin())
        assert exc.status_code == 400

        mockLogin.assert_called_once_with(self.criaBody())
        mockAutenticar.assert_not_called()
        mockCriarToken.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testErroEmailEOuSenhaIncorretos(self, mockCriarToken, mockAutenticar, mockLogin):

        mockAutenticar.side_effect = ErroEmailEOuSenhaIncorretos()

        with pytest.raises(HTTPException) as e:
            CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailEOuSenhaIncorretos())
        assert exc.status_code == 401

        mockLogin.assert_called_once_with(self.criaBody())
        mockAutenticar.assert_called_once_with(mockLogin.return_value)
        mockCriarToken.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testErroEmailNaoEncontrado(self, mockCriarToken, mockAutenticar, mockLogin):

        mockAutenticar.side_effect = ErroEmailNaoEncontrado()

        with pytest.raises(HTTPException) as e:
            CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroEmailNaoEncontrado())
        assert exc.status_code == 404

        mockLogin.assert_called_once_with(self.criaBody())
        mockAutenticar.assert_called_once_with(mockLogin.return_value)
        mockCriarToken.assert_not_called()

    @patch.object(Login, 'fromDict')
    @patch.object(UCLogin, 'autenticarLogin')
    @patch.object(UCCriarToken, '__call__')
    def testErroInesperado(self, mockCriarToken, mockAutenticar, mockLogin):

        mockAutenticar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CLogarFastApi(Mock(), Mock(), Mock())(self.criaBody())

        exc = e.value
        assert exc.detail == str(ErroInesperado())
        assert exc.status_code == 500


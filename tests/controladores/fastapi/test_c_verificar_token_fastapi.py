import pytest
from unittest.mock import Mock, patch
from fastapi import HTTPException

from src.controladores.fastapi.c_verificar_token_fastapi import CVerificarTokenFastAPI
from src.usecases.uc_verificar_token import UCVerificarToken


class TestCVerificarTokenFastapi:

    @patch.object(UCVerificarToken, '__call__')
    def testRespostaOK(self, mockVerificar):

        mockVerificar.return_value = "content"

        c = CVerificarTokenFastAPI(Mock())("body")

        assert c.body.decode() == str(mockVerificar.return_value)
        assert c.status_code == 200

        mockVerificar.assert_called_once_with("body")

    @patch.object(UCVerificarToken, '__call__')
    def testRespostaErro(self, mockVerificar):
        mockVerificar.side_effect = Exception("erro")

        with pytest.raises(HTTPException) as e:
            CVerificarTokenFastAPI(Mock())("body")

        exc = e.value
        assert exc.detail == str(Exception("erro"))
        assert exc.status_code == 401

        mockVerificar.assert_called_once_with("body")

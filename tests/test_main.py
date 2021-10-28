from fastapi.testclient import TestClient

from src.controladores.fastapi.http.respostas import ResRoot
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import *
from src.config.enums.deployment import KEY
from src.main import main


(_, ctrl) = main(repo=ProjConfig.getDeployment()[KEY.TIPO_REPOSITORIO.value], ctrl=ProjConfig.getDeployment()[KEY.TIPO_CONTROLADOR.value])
client = TestClient(ctrl.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ResRoot(deployment=ProjConfig.getDeployment(), controlador=ProjConfig.getFastapi())

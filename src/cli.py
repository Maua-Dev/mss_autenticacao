import argparse
import os
import sys

# Criar o parser
from src.config.enums.deployment import REPOSITORIO, KEY
from src.config.proj_config import ProjConfig

class Cli():
    parser: argparse.ArgumentParser
    args: argparse.Namespace

    def __init__(self):
        myParser = argparse.ArgumentParser(description='Inicializa a execução do mss')

        # Adiciona os argumentos opcionais
        myParser.add_argument('-repo',
                               type=str,
                               default=ProjConfig.getDeployment()[KEY.TIPO_REPOSITORIO.value],
                               help='Especifica o repositório que será utilizado. Default=%(default)s')

        myParser.add_argument('-ctrl',
                               type=str,
                               default=ProjConfig.getDeployment()[KEY.TIPO_CONTROLADOR.value],
                               help='Especifica o repositório que será utilizado. Default=%(default)s')

        myParser.add_argument('-porta',
                              type=int,
                              default=ProjConfig.getFastapi()['porta'],
                              help='Especifica a porta que será utilizada. Default=%(default)s')

        self.parser = myParser
        self.args = myParser.parse_args()


    def getArgs(self):
        return self.args

    def getRepo(self):
        return self.args.repo

    def getCtrl(self):
        return self.args.ctrl

    def getPorta(self):
        return self.args.porta
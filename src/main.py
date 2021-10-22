import uvicorn

from src.cli import Cli
from src.init import Init


def main(repo: str, ctrl: str):
    (_, _ctrl) = Init()(tipo_repo=repo, tipo_ctrl=ctrl)

    return _, _ctrl


if __name__ == '__main__':
    cli = Cli()
    (_, ctrl) = main(repo=cli.getRepo(), ctrl=cli.getCtrl())
    ctrl.start()(app=ctrl.app, host=ctrl.host, porta=cli.getPorta())
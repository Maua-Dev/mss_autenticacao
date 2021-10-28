import uvicorn


class Start():

    def __call__(self, app, host, porta):
        uvicorn.run(app=app, host=host, port=porta)
from flask import Flask

import api
from controller import Controller

controller = Controller()


def create_app():
    app = Flask(__name__)
    app.add_url_rule("/new", view_func=api.CreateBoard.as_view('create_board'))
    app.add_url_rule("/set", view_func=api.SetState.as_view('set_state'))
    app.add_url_rule("/tick", view_func=api.Tick.as_view('tick'))
    return app


if __name__ == "__main__":
    create_app().run(debug=True)

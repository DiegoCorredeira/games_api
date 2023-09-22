from flask import Flask
from flask_restful import Api, Resource
from resources.games import Playstation, Xbox, AllGames, GamesId

app = Flask(__name__)
api = Api(app)


api.add_resource(Playstation, '/games/playstation')
api.add_resource(Xbox, '/games/xbox')
api.add_resource(AllGames, '/games')
api.add_resource(GamesId, '/games/<string:plataform>/<int:game_id>')

if __name__ == '__main__':
    app.run(debug=True)

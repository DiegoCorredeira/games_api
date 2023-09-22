from hmac import new
from flask import json
from flask_restful import Resource, reqparse
from models.games import GamesModel


playstation_games = [
    {
        'id': 1,
        'name': 'God of War',
        'genre': 'Action-adventure',
        'platform': ['Playstation', 'PC'],
        'year': '2018'
    },
    {
        'id': 2,
        'name': 'The Last of Us',
        'genre': 'Action-adventure',
        'platform': ['Playstation', 'PC'],
        'year': '2013'
    },
    {
        'id': 3,
        'name': 'Uncharted 4',
        'genre': 'Action-adventure',
        'platform': ['Playstation', 'PC'],
        'year': '2016'
    },

]
xbox_games = [
    {
        'id': 1,
        'name': 'Halo',
        'genre': 'Action-adventure',
        'platform': ['Xbox', 'PC'],
        'year': '2001'
    },
    {
        'id': 2,
        'name': 'Gears of War',
        'genre': 'Action-adventure',
        'platform': ['Xbox', 'PC'],
        'year': '2006'
    },
    {
        'id': 3,
        'name': 'Forza Horizon',
        'genre': 'Racing',
        'platform': ['Xbox', 'PC'],
        'year': '2012'
    },

]

class Playstation(Resource):
    def get(self):
        return {'Playstation': playstation_games}

class Xbox(Resource):
    def get(self):
        return {'Xbox': xbox_games}
    
class AllGames(Resource):
    def get(self):
        all_games = {'Playstation Games': playstation_games, 'Xbox Games': xbox_games}
        return all_games



class GamesId(Resource):
    keys_args = reqparse.RequestParser()
    keys_args.add_argument('name', type=str, help='Name of the game')
    keys_args.add_argument('genre', type=str, help='Genre of the game')
    keys_args.add_argument('platform', type=str, help='Platform of the game')
    keys_args.add_argument('year', type=str, help='Year of the game')
    
    def get(self,platform, game_id):
        games = playstation_games if platform == 'playstation' else xbox_games
        game = next((game for game in games if game['id'] == game_id), None)
        if game:
            return game, 200
        return {'Game': None}, 404
     
    def post(self, platform, game_id):
        args = GamesId.keys_args.parse_args()
        game = GamesModel(game_id, args['name'], args['genre'], args['platform'], args['year'])
        if platform == 'playstation':
            playstation_games.append(game.json())
        elif platform == 'xbox':
            xbox_games.append(game.json())
        return game.json(), 201
    
    def put(self, platform, game_id):
        args = GamesId.keys_args.parse_args()
        game = next((game for game in playstation_games if game['id'] == game_id), None)
        if game:
            game.update(args)
            return game, 200
        return {'Game': None}, 404
    
    def delete(self, platform, game_id):
        games = playstation_games if platform == 'playstation' else xbox_games
        game = next((game for game in games if game['id'] == game_id), None)
        if game:
            games.remove(game)
            return {'message': 'Game deleted'}
        return {'message': 'Game not found'}, 404
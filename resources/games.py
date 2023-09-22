from flask import json
from flask_restful import Resource, reqparse


playstation_games = [
    {
        'id': 1,
        'name': 'God of War',
        'genre': 'Action-adventure',
        'plataform': ['Playstation', 'PC'],
        'year': '2018'
    },
    {
        'id': 2,
        'name': 'The Last of Us',
        'genre': 'Action-adventure',
        'plataform': ['Playstation', 'PC'],
        'year': '2013'
    },
    {
        'id': 3,
        'name': 'Uncharted 4',
        'genre': 'Action-adventure',
        'plataform': ['Playstation', 'PC'],
        'year': '2016'
    },
    {
        'id': 4,
        'name': 'Horizon Zero Dawn',
        'genre': 'Action-adventure',
        'plataform': ['Playstation', 'PC'],
        'year': '2017'
    },
    {
        'id': 5,
        'name': 'Marvels Spider-Man', 
        'genre': 'Action-adventure',
        'plataform': ['Playstation', 'PC'],
        'year': '2018'
    },
    {
        'id': 6,
        'name': 'Bloodborne',
        'genre': 'Action-adventure',
        'plataform': ['Playstation', 'PC'],
        'year': '2015'
    },
    {
        'id': 7,
        'name': 'Ghost of Tsushima',
        'genre': 'Action-adventure',
        'plataform': ['Playstation', 'PC'],
        'year': '2020',
    }

]
xbox_games = [
    {
        'id': 1,
        'name': 'Halo',
        'genre': 'Action-adventure',
        'plataform': ['Xbox', 'PC'],
        'year': '2001'
    },
    {
        'id': 2,
        'name': 'Gears of War',
        'genre': 'Action-adventure',
        'plataform': ['Xbox', 'PC'],
        'year': '2006'
    },
    {
        'id': 3,
        'name': 'Forza Horizon',
        'genre': 'Racing',
        'plataform': ['Xbox', 'PC'],
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
    keys_args.add_argument('plataform', type=str, help='Plataform of the game')
    keys_args.add_argument('year', type=str, help='Year of the game')
    
    def get(self,plataform, game_id):
        games = None
        if plataform == 'playstation':
            games = playstation_games
        elif plataform == 'xbox':
            games = xbox_games
        if games:
            for game in games:
                if game['id'] == game_id:
                    return game, 200
        return {'Game': None}, 404
     
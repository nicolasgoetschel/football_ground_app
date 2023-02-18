from db.run_sql import run_sql

from models.football_ground import FootballGround
from models.league import League
from models.country import Country
import repositories.league_repository as league_repository
import repositories.football_ground_repository as football_ground_repository


def save(league):
    sql = """INSERT INTO leagues (name, logo, football_grounds_id) 
    VALUES (%s, %s, %s) RETURNING *"""
    values = [league.name, league.logo, league.football_grounds.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    league.id = id
    return league
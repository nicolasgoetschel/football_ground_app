from db.run_sql import run_sql

from models.football_ground import FootballGround
from models.league import League
from models.country import Country
import repositories.league_repository as league_repository
import repositories.football_ground_repository as football_ground_repository


def save(country):
    sql = """INSERT INTO countries (name, flag, leagues_id) 
    VALUES (%s, %s, %s) RETURNING *"""
    values = [country.name, country.flag, country.leagues.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country
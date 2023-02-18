from db.run_sql import run_sql

from models.football_ground import FootballGround
from models.league import League
from models.country import Country


def save(football_ground):
    sql = """INSERT INTO grounds (name, team, location, capacity,
          visited) VALUES (%s, %s, %s, %s, %s) RETURNING *"""
    values = [football_ground.name, football_ground.team, football_ground.location, 
          football_ground.capacity, football_ground.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    football_ground.id = id
    return football_ground


from flask import Flask, Blueprint, render_template, request, redirect
from repositories import football_ground_repository
from models.football_ground import FootballGround

football_grounds_blueprint = Blueprint("football_grounds", __name__)
from flask import Flask, Blueprint, render_template, request, redirect
from repositories import league_repository
from models.league import League

leagues_blueprint = Blueprint("leagues", __name__)
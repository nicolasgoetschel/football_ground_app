from flask import Flask, Blueprint, render_template, request, redirect
from repositories import country_repository
from models.country import Country

countries_blueprint = Blueprint("countries", __name__)



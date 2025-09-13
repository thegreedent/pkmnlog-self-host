from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Playthrough, Entry
from datetime import date

main = Blueprint('main', __name__)

@main.route('/')
def index():
    playthroughs = Playthrough.query.order_by(Playthrough.updated_at.desc()).all()
    return render_template('index.html', playthroughs=playthroughs)
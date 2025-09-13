from app import db
from app.enums import Game, Category
from datetime import date

class Playthrough(db.Model):
    '''
    Represents a playthrough of a Pokémon game.

    Tracks basic information about a player's journey through a specific
    Pokemon game, including the game title, which game is being played,
    and when the playthrough started.

    Attributes:
        id (int): Primary key for the playthrough record.
        title (str): User-defined name for this playthrough (max 120 characters).
        game (Game): The Pokemon game being played (enum value).
        start_date (date): Date when the playthrough began (defaults to today).
        created_at (datetime): Timestamp when the playthrough record was created.
        updated_at (datetime): Timestamp when the playthrough record was last updated.
        entries (list[Entry]): Collection of log entries for this playthrough.
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    game = db.Column(db.Enum(Game), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    entries = db.relationship('Entry', backref='playthrough', lazy=True)

class Entry(db.Model):
    '''
    Represents a single log entry within a playthrough.

    Captures specific events, achievements, or milestones during a Pokemon
    game playthrough, such as catching Pokemon or earning badges.

    Attributes:
        id (int): Primary key for the entry record.
        playthrough_id (int): Foreign key linking to the parent playthrough.
        title (str): Brief title describing the entry (max 120 characters).
        category (Category): Type of entry (enum value).
        description (str, optional): Detailed description of the entry event.
        created_at (datetime): Timestamp when the entry record was created.
        updated_at (datetime): Timestamp when the entry record was last updated.
    '''
    id = db.Column(db.Integer, primary_key=True)
    playthrough_id = db.Column(db.Integer, db.ForeignKey('playthrough.id'), nullable=False)

    title = db.Column(db.String(120), nullable=False)
    category = db.Column(db.Enum(Category), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

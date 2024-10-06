from flask.cli import FlaskGroup
from app import create_app, db
from config.config import Config

cli = FlaskGroup(create_app=lambda: create_app(Config))

@cli.command("init_db")
def init_db():
    db.create_all()
    print("Database initialized")

if __name__ == "__main__":
    cli()
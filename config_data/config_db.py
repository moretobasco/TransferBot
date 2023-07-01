from dataclasses import dataclass
from environs import Env


@dataclass
class DBConfig:
    db_user: str
    db_password: str
    db_host: str
    db_database: str
    db_port: str


def load_db_config(path: str | None = None) -> DBConfig:
    env = Env()
    env.read_env(path)
    return DBConfig(
        db_user=env('DB_USER'),
        db_password=env('DB_PASSWORD'),
        db_database=env('DB_DATABASE'),
        db_host=env('DB_HOST'),
        db_port=env('DB_PORT')
    )

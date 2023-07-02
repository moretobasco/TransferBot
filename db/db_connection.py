import asyncio

import asyncpg
from config_data.config_db import DBConfig, load_db_config


async def connect_db() -> asyncpg.connect():
    # Установка соединения с базой данных
    # Перейти на переменные окружения Postgres, например, PGHOST
    db_config: DBConfig = load_db_config()
    db_user = db_config.db_user
    db_password = db_config.db_password
    db_database = db_config.db_database
    db_host = db_config.db_host
    db_port = db_config.db_port

    conn = await asyncpg.connect(
        user=db_user,
        password=db_password,
        database=db_database,
        host=db_host,
        port=db_port
    )

    return conn

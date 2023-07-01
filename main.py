import asyncio
import asyncpg
from config_data.config_db import DBConfig, load_db_config
from db.db_work import create_table


async def work_with_db():
    # Установка соединения с базой данных
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

    await create_table(conn=conn)

if __name__ == '__main__':
    asyncio.run(work_with_db())

# asyncio.get_event_loop().run_until_complete(work_with_db())
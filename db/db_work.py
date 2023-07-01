import asyncio
import asyncpg
from config_data.config_db import DBConfig, load_db_config



async def create_table(conn):
    # Создание таблицы
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
    '''
    await conn.execute(create_table_query)

    # Вставка данных в таблицу
    insert_query = '''
        INSERT INTO my_table (name, age) VALUES ($1, $2);
    '''
    await conn.execute(insert_query, 'John Moo', 424)

    # Закрытие соединения
    await conn.close()




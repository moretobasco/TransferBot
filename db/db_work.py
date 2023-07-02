import asyncio
import asyncpg
from config_data.config_db import DBConfig, load_db_config
import datetime
from db.db_connection import connect_db


async def create_table():
    conn = await connect_db()
    # Создание таблицы
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            date DATE,
            status VARCHAR(10),
            available_seats INTEGER
        );
    '''
    await conn.execute(create_table_query)

    # Вставка данных в таблицу
    insert_query = '''
        INSERT INTO my_table (date, status, available_seats) VALUES ($1, $2, $3);
    '''
    date_str = '2023-06-01'
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    await conn.execute(insert_query, date_obj, 'open', 8)

    # Закрытие соединения
    await conn.close()

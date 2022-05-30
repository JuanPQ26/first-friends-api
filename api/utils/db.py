# database
import psycopg2
# utils
from api.utils import env


def create_postgres_connection():
    environment = env.get_env("DB_ENV")

    if environment == "prd":
        database = env.get_env("DB_NAME_PRD")
        username = env.get_env("DB_USER_PRD")
        password = env.get_env("DB_PASS_PRD")
        host = env.get_env("DB_HOST_PRD")
        port = env.get_env("DB_PORT_PRD")

        dsn_str = f"dbname={database} " \
                  f"user={username} " \
                  f"password={password} " \
                  f"host={host} " \
                  f"port={port} "

        connection = psycopg2.connect(dsn_str)
    else:
        database = env.get_env("DB_NAME_DEV", "friends_dev")
        username = env.get_env("DB_USER_DEV", "postgres")
        password = env.get_env("DB_PASS_DEV", "")
        host = env.get_env("DB_HOST_DEV", "localhost")
        port = env.get_env("DB_PORT_DEV", "5432")

        dsn_str = f"dbname={database} " \
                  f"user={username} " \
                  f"password={password} " \
                  f"host={host} " \
                  f"port={port} "

        print(dsn_str)

        connection = psycopg2.connect(dsn_str)

    return connection


def execute_postgres_query(query: str) -> None:
    connection = create_postgres_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        raise e
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def execute_postgres_select(query: str, one=False) -> dict | list | None:
    connection = create_postgres_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(query)

        v = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        result = (v[0] if v else None) if one else v
        return result
    except Exception as e:
        raise e
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

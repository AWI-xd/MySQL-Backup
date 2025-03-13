import pymysql

backup_file = 'my_database_backup.sql'


def create_backup(db_host, db_user, db_name, db_password, db_port):
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, port=db_port)
    cursor = connection.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    with open(backup_file, 'w', encoding='utf-8') as f:
        for table in tables:
            table_name = table[0]
            print(f"Сохранение таблицы: {table_name}")

            cursor.execute(f"SHOW CREATE TABLE {table_name}")
            create_table = cursor.fetchone()[1]
            f.write(f"{create_table};\n\n")

            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            for row in rows:
                values = ", ".join([f"'{str(value)}'" if value is not None else 'NULL' for value in row])
                f.write(f"INSERT INTO {table_name} VALUES ({values});\n")
            f.write("\n")

    cursor.close()
    connection.close()

    print(f"Бэкап базы данных {db_name} успешно создан в файле {backup_file}")
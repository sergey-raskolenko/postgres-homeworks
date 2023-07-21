"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

# Создание переменных для указания пути к конкретному файлу
dir_name = 'north_data'
customers_file = 'customers_data.csv'
employees_file = 'employees_data.csv'
orders_file = 'orders_data.csv'
dir_path = os.path.join(os.path.dirname(__file__), dir_name)
customers_file = os.path.join(dir_name, customers_file)
employees_file = os.path.join(dir_name, employees_file)
orders_file = os.path.join(dir_name, orders_file)

if __name__ == '__main__':
    # Получение данных значений из .csv файлов
    with open(customers_file, newline='') as file:
        customers_csv = csv.DictReader(file)
        customers_data = [tuple(item.values()) for item in customers_csv]
    with open(employees_file, newline='') as file:
        employees_csv = csv.DictReader(file)
        employees_data = [tuple(item.values()) for item in employees_csv]
    with open(orders_file, newline='') as file:
        orders_csv = csv.DictReader(file)
        orders_data = [tuple(item.values()) for item in orders_csv]
    # Создание подключения к базе данных, запись в таблицы
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='3881125')
    try:
        with conn:
            with conn.cursor() as cur:
                for item in customers_data:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", item)
            with conn.cursor() as cur:
                for item in employees_data:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", item)
            with conn.cursor() as cur:
                for item in orders_data:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", item)
    finally:
        conn.close()

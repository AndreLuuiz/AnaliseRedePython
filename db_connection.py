import sqlite3
import json

def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS network_stats (
            src_ip TEXT,
            dst_ip TEXT,
            proto TEXT,
            size INTEGER
        )
    ''')
    conn.commit()
    return conn

def insert_stats(conn, stats):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO network_stats (src_ip, dst_ip, proto, size)
        VALUES (?, ?, ?, ?)
    ''', (stats['src_ip'], stats['dst_ip'], stats['proto'], stats['size']))
    conn.commit()

def save_stats_to_db(file_name, db_name):
    conn = connect_db(db_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
        for stats in data:
            insert_stats(conn, stats)
    conn.close()
import sqlite3

DATABASE_FILE = 'cabin_reservation.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cabins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT NOT NULL,
            cabin_id INTEGER NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL,
            FOREIGN KEY (cabin_id) REFERENCES cabins (id)
        )
    ''')

    conn.commit()
    conn.close()

def seed_cabins():
    """Insert predefined cabins if they do not exist."""
    cabins = ["Raccoon Holler", "Chipmunk Ridge", "Flamingos Paradise"]

    conn = get_db_connection()
    cursor = conn.cursor()

    for cabin in cabins:
        cursor.execute("INSERT OR IGNORE INTO cabins (name) VALUES (?)", (cabin,))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    seed_cabins()  

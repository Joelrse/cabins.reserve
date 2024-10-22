
from databases import get_db_connection

class Cabin:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def create(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cabins (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(cabin_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cabins WHERE id = ?", (cabin_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cabins")
        cabins = cursor.fetchall()
        conn.close()
        return cabins

    @staticmethod
    def find_by_id(cabin_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cabins WHERE id = ?", (cabin_id,))
        cabin = cursor.fetchone()
        conn.close()
        return cabin

class Reservation:
    def __init__(self, id=None, guest_name=None, cabin_id=None, check_in=None, check_out=None):
        self.id = id
        self.guest_name = guest_name
        self.cabin_id = cabin_id
        self.check_in = check_in
        self.check_out = check_out

    def create(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservations (guest_name, cabin_id, check_in, check_out)
            VALUES (?, ?, ?, ?)
        """, (self.guest_name, self.cabin_id, self.check_in, self.check_out))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(reservation_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        """Fetch all reservations along with their cabin names."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT reservations.id, reservations.guest_name, cabins.name, reservations.check_in, reservations.check_out
            FROM reservations
            JOIN cabins ON reservations.cabin_id = cabins.id
        """)
        reservations = cursor.fetchall()
        conn.close()
        return reservations

    @staticmethod
    def find_by_id(reservation_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,))
        reservation = cursor.fetchone()
        conn.close()
        return reservation

    @staticmethod
    def get_by_cabin_id(cabin_id):
        """Fetch reservations by cabin id."""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT reservations.id, reservations.guest_name, cabins.name, reservations.check_in, reservations.check_out
            FROM reservations
            JOIN cabins ON reservations.cabin_id = cabins.id
            WHERE reservations.cabin_id = ?
        """, (cabin_id,))
        reservations = cursor.fetchall()
        conn.close()
        return reservations

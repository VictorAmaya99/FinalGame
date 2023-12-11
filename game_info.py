
import sqlite3

class Database:
    def __init__(self, db_name='game_data.db'):
        self.db_name = db_name

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS jugadores (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            jugador_id INTEGER,
                            nivel INTEGER,
                            score INTEGER
                        )''')

        conn.commit()
        conn.close()

    def save_game_data(self, score):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO jugadores (jugador_id, nivel, score) VALUES (?, ?, ?)", (score))

        conn.commit()
        conn.close()

    def load_game_data(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Obtener los tres últimos juegos de cada nivel para cada jugador
        query = query = '''SELECT j1.*
                FROM jugadores j1
                WHERE j1.id IN (
                    SELECT j2.id
                    FROM jugadores j2
                    WHERE j2.jugador_id = j1.jugador_id AND j2.nivel = j1.nivel
                    ORDER BY j2.id DESC
                    LIMIT 3
                )
                ORDER BY j1.jugador_id, j1.nivel, j1.id DESC'''
        cursor.execute(query)
        jugadores_data = cursor.fetchall()

        conn.close()

        return jugadores_data
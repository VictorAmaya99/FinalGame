
import sqlite3

class DBManager:
    def __init__(self, db_name='ranking.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('DROP TABLE IF EXISTS ranking')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                level INTEGER NOT NULL DEFAULT 1
            )
        ''')

        conn.commit()
        conn.close()    

    def save_score(self, level, score):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO ranking (level, score)
            VALUES (?, ?)
        ''', (level, score))

        conn.commit()
        conn.close()

    def get_latest_scores(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT level, MAX(score) AS max_score
            FROM ranking
            GROUP BY level
        ''')

        latest_scores = cursor.fetchall()
        conn.close()

        return latest_scores

    def get_score_by_level(self, level):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT score
            FROM ranking
            WHERE level = ?
        ''', (level,))

        score_data = cursor.fetchone()
        conn.close()

        return score_data[0] if score_data else None

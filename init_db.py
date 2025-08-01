import sqlite3
import os

def init_db(db_path="quantum_genesis.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Drop existing table if it exists
    cursor.execute("DROP TABLE IF EXISTS genesis_blocks")
    
    # Create new table with all columns
    cursor.execute('''CREATE TABLE genesis_blocks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    query TEXT,
                    quantum_state TEXT,
                    classical_physics TEXT,
                    relativity_metrics TEXT,
                    fractal_dna TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    visualization_path TEXT
                  )''')
    
    conn.commit()
    conn.close()
    print(f"Database initialized at {db_path}")

if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), "quantum_genesis.db")
    init_db(db_path)

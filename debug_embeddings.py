

import mysql.connector
import numpy as np

# Connect to your database
conn = mysql.connector.connect(
    host="LOCALHOST",
    user="root",
    password="",
    database="courses1"
)
cursor = conn.cursor()

# Fetch one embedding
cursor.execute("SELECT embedding FROM udemy_courses_ WHERE embedding IS NOT NULL LIMIT 10")
for idx, (embedding_blob,) in enumerate(cursor.fetchall(), start=1):
    try:
        embedding = np.frombuffer(embedding_blob, dtype=np.float32)
        print(f"Embedding {idx}: Shape = {embedding.shape}")
    except Exception as e:
        print(f"Error deserializing embedding {idx}: {e}")

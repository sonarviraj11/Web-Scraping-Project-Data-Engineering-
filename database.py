import sqlite3

def save_to_db(df, db_path="prices.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("products", conn, if_exists="replace", index=False)
    conn.close()

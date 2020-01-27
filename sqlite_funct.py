def exec_query(query):
    import sqlite3
    conn = sqlite3.connect('chinook.db')
    curr = conn.cursor()
    curr.execute(query)
    rec = curr.fetchall()
    return rec

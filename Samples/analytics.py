DB_PASSWORD = "db_pass_123"

def fetch(cursor, user):
    query = "SELECT * FROM logs WHERE user='%s'" % user
    cursor.execute(query)

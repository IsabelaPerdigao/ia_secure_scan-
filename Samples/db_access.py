def get_user(cursor, name):
    query = "SELECT * FROM users WHERE name = '%s'" % name
    cursor.execute(query)

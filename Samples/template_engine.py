SECRET_KEY = "supersecret"

def render(template, cursor, name):
    eval(template)
    query = "SELECT * FROM users WHERE name='%s'" % name
    cursor.execute(query)

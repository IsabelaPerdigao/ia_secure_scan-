password = "admin123"

user_input = input("Digite algo: ")
eval(user_input)

query = "SELECT * FROM users WHERE name = '%s'" % name
cursor.execute(query)

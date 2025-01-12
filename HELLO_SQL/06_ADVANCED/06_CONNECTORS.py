# 5:48:51
import mysql.connector


def get_user(user):

    #    config = {
    #        "host": "127.0.0.1",
    #        "port": "3306",
    #        "database": "main_database",
    #        "user": "root",
    #        "password": "root"
    #    }

    config = {
        "host": "bw9awnn511ikmxpl1b0q-mysql.services.clever-cloud.com",
        "port": "3306",
        "database": "bw9awnn511ikmxpl1b0q",
        "user": "uu1uf6txvy80i1ng",
        "password": "d4BdTLrtQvCYbH3PkAAZ"
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    if user == "":
        query = "SELECT * FROM users;"
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()

    else:
        query = "SELECT * FROM users WHERE name = %s;"
        print(query)
        cursor.execute(query, (user,))
        result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


get_user("")

# ## Se puede pasar querys atraves de los parametros de ejecucion, y a esto se le conoce como sql injection (o al menos uno de sus metodos)
# get_user("'; UPDATE users SET age = '15' WHERE user_id = 1; --")

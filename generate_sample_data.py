from random import randint, random, uniform
import pandas as pd

n = 20

def produce_stmt(table_name, columns, data):
    result = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES"
    for row in data:
        temp = ""
        for x in row:
            if isinstance(x, int):
                temp += str(x) + ", "
            elif isinstance(x, str):
                temp += f""""{x}", """
            elif isinstance(x, float):
                temp += str(x) + ", "
            elif x is None:
                temp += "NULL, "
            else:
                print("error!!!!!")
                exit(1)
        temp = temp[:-2]

        result += f" ({temp}),"
    result = result[:-1] + ';'
    print(result)

import random
import time
    
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)

persons1 = [[x, f'employee{x}', f'pwd{x}', random_date("2020-01-01 00:00:01", "2023-01-01 00:00:01", random.random())] for x in range(1, n+1)]
persons2 = [[n+x, f'user{x}', f'pwd{x}', random_date("2020-01-01 00:00:01", "2023-01-01 00:00:01", random.random())] for x in range(1, n+1)]
persons = persons1 + persons2

produce_stmt("Person", ['id', 'username', 'pwd', 'last_log_in'], persons)

permissions = [[x, f"permission{x}"] for x in range(1, 11)]

produce_stmt("Permission", ['id', 'name'], permissions)

employees = [[x, round(uniform(3000, 5000), 2), round(uniform(35,40), 1)] for x in range(1, n+1)]

produce_stmt("Employee", ['id', 'salary', 'working_hours'], employees)

permits = [[x, randint(1, 10)] for x in range(1, len(employees)+1)] + [[randint(1, len(employees)), randint(1,10)] for x in range(10)]

produce_stmt("Permits", ['employee_id', 'permission_id'], permits)

users = [[n+x, randint(0, n * 2), f"level{randint(1, 5)}"] for x in range(1, n+1)]

produce_stmt("User", ['id', 'activeness', 'level'], users)

import datetime

start_date = datetime.date(1950, 1, 1)
end_date   = datetime.date(2022, 1, 1)
num_days   = (end_date - start_date).days

celebrity1 = [[x, f'director{x}', f"nationality{randint(1, 10)}" if randint(0,2) == 0 else None, (start_date + datetime.timedelta(days=randint(1, num_days))).strftime("%Y-%m-%d") if randint(0,1) else None, f"summary{x}" if randint(0,1) else None] for x in range(1, n + 1)]
celebrity2 = [[n+x, f'actor{x}', f"nationality{randint(1, 10)}" if randint(0,2) == 0 else None, (start_date + datetime.timedelta(days=randint(1, num_days))).strftime("%Y-%m-%d") if randint(0,1) else None, f"summary{n+x}" if randint(0,1) else None] for x in range(1, n * 2 + 1)]
celebrity = celebrity1 + celebrity2

produce_stmt("Celebrity", ['id', 'name', 'nationality', 'birth', 'summary'], celebrity)

director = [[x, f"school{randint(1, 10)}" if randint(0, 2) else None] for x in range(1, n+1)]

produce_stmt("Director", ['id', 'graduation'], director)

movies = [[x, f'movie{x}', f'region{randint(1, n * 2)}', randint(1800, 2023), f'introduction{x}', 0.0, x] for x in range(1, n + 1)] + [[x+n, f'movie{x+n}', f'region{randint(1, n * 2)}', randint(1800, 2023), f'introduction{x+n}', 0.0, randint(1, n)] for x in range(1, n + 1)]

produce_stmt("Movie", ['id', 'name', 'region', 'year', 'introduction', 'avg_rate', 'director_id'], movies)

category = [[x, f"category{randint(1, 10)}"] for x in range(1, n * 2 + 1)] + [[randint(1, n*2), f"category{randint(1, 10)}"] for x in range(1, n + 1)]

produce_stmt("Movie_category", ['movie_id', 'category'], category)

actors = [[x, f"organization{randint(1, 20)}" if randint(0, 1) else None] for x in range(n + 1, n * 3 + 1)]

produce_stmt("Actor", ['id', 'organization'], actors)

acts = [[x, n * 2 - (x - n) + 1] for x in range(n + 1, n * 3)] + [[randint(n + 1, n * 3), randint(1, n*2)] for x in range(n + 1, n * 3 + 1)]

produce_stmt("Acts", ['actor_id', 'movie_id'], acts)

ratings = []
temp = [[0,0] for x in range(1, n * 2 + 1)] # sum, count
rateby = []
for x in range(1, n*2 + 1):
    val = randint(1, 10)
    movie_id = randint(1, n * 2)
    user_id = randint(21, 39)
    rateby.append([movie_id, user_id])
    temp[movie_id-1][0] += val
    temp[movie_id-1][1] += 1
    ratings.append([x, random_date("2023-01-02 00:00:01", "2023-03-01 00:00:01", random.random()), val, f"comment{x}" if randint(0,2) else None, movie_id, user_id])

produce_stmt("RateBy", ['movie_id', 'user_id'], rateby)

produce_stmt("Rating", ['id', 'time', 'value', 'comment', 'movie_id', 'user_id'], ratings)

for x in range(n*2):
    movies[x][5] = temp[x][0] / temp[x][1] if temp[x][1] != 0 else 0.0
    print(f"Update Movie SET avg_rate={round(movies[x][5], 2)} WHERE id={movies[x][0]};")

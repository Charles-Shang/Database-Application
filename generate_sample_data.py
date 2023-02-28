from random import randint, random

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
            else:
                print("error!!!!!")
                exit(1)
        temp = temp[:-2]

        result += f" ({temp}),"
    result = result[:-1] + ';'
    print(result)

users = [[x, f'user{x}'] for x in range(1, n+1)]
movies = [[x, f'movie{x}', f'region{randint(1, n * 2)}', randint(2000, 2023), f'category{randint(1, n*2)}', 0, f'summary{x}'] for x in range(1, n+1)]
rates =  [[x, round(random() * 10, 2), randint(1, n), randint(1,n)] for x in range(1, n * 2 + 1)]
directors = [[x, f'director{x}', randint(1950, 2010)] for x in range(1, n+1)]
actors = [[x, f'actor{x}', randint(1950, 2010)] for x in range(1, n * 2 + 1)]

temp = [[0,0] for x in range(n)]
for i in range(n * 2):
    temp[rates[i][2]-1][0] += 1
    temp[rates[i][2]-1][1] += rates[i][1]

for i in range(n):
    movies[i][5] = round(temp[i][1] / temp[i][0], 2) if(temp[i][0] != 0) else 0


produce_stmt("USER", ['userID', 'name'], users)

produce_stmt("MOVIE", ['movieID', 'name', 'region', 'year', 'category', 'rates', 'summary'], movies)

produce_stmt("RATES", ['rateID', 'rate', 'movieID', 'userID'], rates)

produce_stmt("DIRECTOR", ['directorID', 'name', 'birthYear'], directors)

produce_stmt("DIRECTS", ['directorID', 'movieID'], [[i, n-i+1] for i in range(n)])

produce_stmt("ACTOR", ['actorID', 'name', 'birthYear'], actors)

produce_stmt("ACTS", ['actorID', 'movieID'], [[i, n - i + 1] if i <= n else [i, randint(1,n)] for i in range(1, n * 2 +1)] + [[randint(1, n*2), randint(1, n)] for i in range(1, n * 2 +1)])
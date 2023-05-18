# import psycopg2
# import sys
# params_connection = {
#         'host': 'localhost',
#         'user': 'postgres',
#         'password': 'qwe123',
#         'database': 'postgres'
#     }
#
# def connection_to_db():
#     return psycopg2.connect(**params_connection)
#
# def auth(self, login, password):
#     print(111)
#     conn = connection_to_db()
#     with conn.cursor() as cursor:
#         cursor.execute(f'select login, password from users')
#         users = cursor.fetchall()
#         for user in users:
#             if user[0] == login and user[1] == password:
#                 self.openMaster(self)
#                 break
#
#  def reg(self, login, password):
#         conn = connection_to_db()
#         is_login = False
#         with conn.cursor() as cursor:
#             cursor.execute(f'select login from users')
#             users = cursor.fetchall()
#             for user in users:
#                 if login in user:
#                     is_login = True
#                     break
#         with conn.cursor() as cursor:
#             if not is_login:
#                 query = f"INSERT INTO users (login, password) VALUES ('{login}', '{password}');"
#                 cursor.execute(query)
#                 conn.commit()
#                 print(f'Зарегистрирован пользователь {login}')
#             else:
#                 print('Логин занят')
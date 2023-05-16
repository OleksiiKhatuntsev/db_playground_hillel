import psycopg2


class BaseRepository:
    def __init__(self):
        self._connection = psycopg2.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432',
            database='hillel_test'
        )
        self._connection.set_session(autocommit=True)
        self._cursor = self._connection.cursor()


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def get_all_users(self):
        self._cursor.execute("SELECT * FROM users;")
        return self._cursor.fetchall()

    def get_user_by_id(self, user_id):
        self._cursor.execute(f"SELECT * FROM users WHERE users.user_id = {user_id};")
        return self._cursor.fetchone()

    def insert_user(self, email, password, age, role_id):
        self._cursor.execute(
            f"INSERT INTO users (email, password, age, role_id) VALUES ('{email}', '{password}', '{age}', '{role_id}');")
        # self.__connection.commit()

    def delete_by_id(self, user_id):
        self._cursor.execute(f"DELETE FROM users WHERE user_id={user_id};")
        # self.__connection.commit()


if __name__ == "__main__":
    rep = UserRepository()
    # rep.insert_user("jonsnow1@gmail.com", "iknownothing123", 15, 2)
    rep.delete_by_id(15)
    print(rep.get_all_users())
    print(rep.get_user_by_id(2))

import psycopg2


class Database:
    def __init__(self, host, user, password, database):
        try:
            self.connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Подключение к базе данных успешно установлено!")
        except psycopg2.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def execute(self, query: str):
        """
        Function for sending data to the database without receiving a response

        :param query: Request body
        """
        try:
            self.cursor.execute(query)
        except psycopg2.Error as e:
            print(f"Ошибка при выполнении запроса: {e}")

    def fetch(self, query: str):
        """
        Function for sending a query to the database with the possibility to receive a response

        :param query: Requests body
        :return []:
        """
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Ошибка при получении результата запроса: {e}")
            return []

    def __del__(self):
        try:
            self.cursor.close()
            self.connection.close()
            print("Подключение к базе данных успешно закрыто")
        except psycopg2.Error as e:
            print(f"Ошибка при закрытии подключения к базе данных: {e}")

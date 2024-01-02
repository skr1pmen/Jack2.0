import json

from database.base_model import Database
from assets.config import DATABASE


class Functions:
    def __init__(self):
        self.db = Database(DATABASE["HOST"], DATABASE["USERNAME"], DATABASE["PASSWORD"], DATABASE["BASENAME"])

    def user_exists(self, user_id: int) -> bool:
        """
        Function for checking the user's existence in the database

        :param user_id: User ID of the User being checked
        :return True or False:
        """
        return bool(self.db.fetch(f"""SELECT COUNT(*) FROM users WHERE chat_id = {user_id}""")[0][0])

    def add_user(self, user_data):
        """
        Function for adding a user to the database

        :param user_data: Object "User" from telegram
        """
        self.db.execute(f"INSERT INTO users (chat_id, first_name, surname, username) "
                        f"VALUES ({user_data.from_user.id}, '{user_data.from_user.first_name}',"
                        f"'.{user_data.from_user.last_name}', '{user_data.from_user.username}')")

    def group_exists(self, chat_id: int) -> bool:
        """
        Function to see if the user's group is specified in the database

        :param chat_id: ID user from telegram
        :return True or False:
        """
        # print(self.db.fetch(f"SELECT \"group\" FROM users WHERE chat_id = {chat_id}")[0][0])
        return bool(self.db.fetch(f"SELECT \"group\" FROM users WHERE chat_id = {chat_id}")[0][0])

    def edit_group(self, chat_id: int, code: int) -> None:
        """
        User group editing function

        :param chat_id: ID user from telegram
        :param code: Code group user
        :return None:
        """
        self.db.execute(f"UPDATE users SET \"group\" = {code} WHERE chat_id = {chat_id}")

    def answer_bell(self):
        """
        Function that outputs college call schedule

        :return bell_text:
        """
        with open("./assets/bell.json", encoding="utf-8") as bell:
            bell = json.load(bell)
            bell_text: str = "Расписание звонков:\n"
            for day in bell:
                bell_text += f"\n<b>{day}</b>:\n"
                for line in bell[f"{day}"]:
                    bell_text += f"<b>{line}</b>: {bell[day][line]}\n"
        return bell_text

    def get_code(self, chat_id: int):
        """
        Function for obtaining user group code from the database

        :param chat_id: ID user from telegram
        :return code: User group code
        """
        return self.db.fetch(f"SELECT \"group\" FROM users WHERE chat_id = {chat_id}")[0][0]

    def new_schedule(self):
        pass

from alchemy.models.user_model import UserModel
from alchemy.session import session


class UserRepository:
    def __init__(self):
        self.__session = session
        self.__model = UserModel

    def get_all(self):
        return self.__session.query(self.__model).all()

if __name__ == "__main__":
    user_repo = UserRepository()
    result = user_repo.get_all()
    for u in result:
        print(u)
        # print(u.role.title)

from alchemy.models.role_model import RoleModel
from alchemy.session import session


class RoleRepository:
    def __init__(self):
        self.__session = session
        self.__model = RoleModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, role_id):
        role = self.__session.get(self.__model, {'role_id': role_id})
        return role

    def add_item(self, role: RoleModel):
        self.__session.add(role)

    def remove_item_by_id(self, role_id):
        role = self.__session.get(self.__model, {'role_id': role_id})
        self.__session.delete(role)



if __name__ == "__main__":
    role_repo = RoleRepository()
    # result = role_repo.get_all_roles()
    # for role in result:
    #     print(role)
    #     print(role.title)

    # role_to_insert = RoleModel(title="test_role")
    # role_repo.add_item(role_to_insert)
    role_repo.remove_item_by_id(5)
    result = role_repo.get_all()
    for r in result:
        print(r)
        print(r.title)
    # test_get_by_id_role = role_repo.get_by_id(1)
    # print(test_get_by_id_role)
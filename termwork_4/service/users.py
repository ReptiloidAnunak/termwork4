from dao.users import UserDAO

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update_partial(data)

    def update_password(self, data):
        return self.dao.update_password(data)

    def delete(self, uid):
        return self.dao.delete(uid)
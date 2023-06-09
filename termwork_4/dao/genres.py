from dao.models.genre import Genre
from config import Config

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def get_all_paginated(self, page):
        pagination = Genre.query.order_by(Genre.name.asc()).paginate(page, per_page=Config.FLASKY_POSTS_PER_PAGE,
                                                                     error_out=False)
        genres = pagination.items
        return genres

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, data):
        gid = data.get("id")
        genre = self.get_one(gid)
        genre.name = data.get("name")
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()



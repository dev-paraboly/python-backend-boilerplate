class OrmHelper:

    @staticmethod
    def toDict(obj):
        d = {}
        for column in obj.__table__.columns:
            d[column.name] = getattr(obj, column.name)
        return d
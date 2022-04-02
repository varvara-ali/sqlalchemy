from datetime import datetime


class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"), nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    jobs = orm.relation("Users")

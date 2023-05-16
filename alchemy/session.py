from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://postgres:admin@localhost/hillel_test')
auto_commit = engine.execution_options(isolation_level='AUTOCOMMIT')
session: Session = sessionmaker(auto_commit)()

#!/usr/bin/python3
"""Script that print first state """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    contain_a = session\
        .query(State).filter(State.name.contains('a')).order_by(State.id)
    for row in contain_a:
        print(f"{row.id}: {row.name}")
    session.close()

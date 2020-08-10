#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa """


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base
    from relationship_state import State
    from relationship_city import City

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(my_user, my_pass, my_db),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    inst_state = State(name="California")

    inst_state.cities = [City(name="San Francsico")]
    session.add(inst_state)

    session.commit()
    session.close()

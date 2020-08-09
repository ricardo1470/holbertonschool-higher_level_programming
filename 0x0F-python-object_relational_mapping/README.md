> # 0x0F. Python - Object-relational mapping
---
| **Filename** | **Description** |
|---|---|
| [0. Get all states](./0-select_states.py) | script that lists all `states` from the database `hbtn_0e_0_usa`  |
| [1. Filter states](./1-filter_states.py) | script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`.  |
| [2. Filter states by user input ](./2-my_filter_states.py) | script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.  |
| [3. SQL Injection... ](./3-my_safe_filter_states.py) | script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` searched (safe from MySQL injection)  |
| [4. Cities by states](./4-cities_by_state.py) | script that lists all `cities` from the database `hbtn_0e_4_usa`  |
| [5. All cities by state](./5-filter_cities.py) | script that takes in the name of a `state` as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`  |
| [6. First state model ](./model_state.py) | python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.  |
| [7. All states via SQLAlchemy](./7-model_state_fetch_all.py) | script that lists all `State` objects from the database `hbtn_0e_6_usa`  |
| [8. First state](./8-model_state_fetch_first.py) | script that prints the first `State` object from the database `hbtn_0e_6_usa` |
| [9. Contains `a` ](./9-model_state_filter_a.py) | script that lists all `State` objects that contain the letter a from the database `hbtn_0e_6_usa`  |
| [10. Get a state](./10-model_state_my_get.py) | script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`  |
| [11. Add a new state](./11-model_state_insert.py) | script that adds the `State` object `“Louisiana”` to the database `hbtn_0e_6_usa` |
| [12. Update a state](./12-model_state_update_id_2.py) | script that changes the name of a `State` object from the database `hbtn_0e_6_usa`  |
| [13. Delete states](./13-model_state_delete_a.py) | script that deletes all `State` objects with a `name` containing the letter a from the database `hbtn_0e_6_usa`  |
| [14. Cities in state](./14-model_city_fetch_by_state.py) | Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.  |
| **Advanced** | **Description** |
| [15. City relationship](./100-relationship_states_cities.py) | script that creates the `State` “California” with the `City` “San Francisco” from the database `hbtn_0e_100_usa`.  |
| [16. List relationship](./101-relationship_states_cities_list.py) | script that lists all `State` objects, and corresponding `City` objects, contained in the database `hbtn_0e_101_usa`  |
| [17. From city](./102-relationship_cities_states_list.py) | script that lists all `City` objects from the database `hbtn_0e_101_usa`  |
|   |   |
---
## License
*<a href="url"><img src="https://cdn4.iconfinder.com/data/icons/logos-3/181/MySQL-512.png" align="middle" width="100" height="60"></a>`Object-relational mapping` is open source and therefore free to download and use without permission.*

<a href="url"><img src="https://www.holbertonschool.com/holberton-logo.png" align="middle" width="100" height="30"></a>

---


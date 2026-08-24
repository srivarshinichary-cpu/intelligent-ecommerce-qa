from utils.database import (
    create_database,
    insert_order,
    get_order
)


def test_create_and_validate_order():

    create_database()

    insert_order(
        1001,
        "Sauce Labs Backpack",
        1,
        29.99,
        "Completed"
    )

    order = get_order(1001)

    assert order is not None

    assert order[0] == 1001
    assert order[1] == "Sauce Labs Backpack"
    assert order[2] == 1
    assert order[3] == 29.99
    assert order[4] == "Completed"

def test_order_not_found():

    create_database()

    order = get_order(9999)

    assert order is None
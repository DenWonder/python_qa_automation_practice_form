import dataclasses

@dataclasses.dataclass
class BookStoreUser:
    user_name: str
    password: str
    first_name: str
    last_name: str

test_book_store_user_1 = BookStoreUser(
    user_name='Spider',
    password='Qwerty123!',
    first_name='Peter',
    last_name='Parker'
)

test_book_store_user_2 = BookStoreUser(
    user_name='ImABatGuy',
    password='<PASSWORD>!',
    first_name='Bruce',
    last_name='Vayne'
)
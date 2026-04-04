import dataclasses
import time

@dataclasses.dataclass
class BookStoreUser:
    user_name: str
    password: str
    first_name: str
    last_name: str

test_book_store_user_1 = BookStoreUser(
    user_name=f'Spider{time.time()}',
    password='Qwerty123!',
    first_name='Peter',
    last_name='Parker'
)

test_book_store_user_2 = BookStoreUser(
    user_name=f'ImABatGuy{time.time()}',
    password='Password123!',
    first_name='Bruce',
    last_name='Vayne'
)
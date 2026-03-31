import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_day: int
    birth_month: str
    birth_year: int
    subjects: list[str]
    hobbies: list[str]
    current_address: str
    state: str
    city: str
    picture: str

test_user_1 = User(
    first_name="Harry",
    last_name="Potter",
    email='harrypotter@mailtohogwards.com',
    gender='Male',
    phone_number='1234567890',
    birth_day=19,
    birth_month='January',
    birth_year=1978,
    subjects=["Maths", "Physics"],
    hobbies=["Sports"],
    current_address='Privet drive, 4',
    state='NCR',
    city='Delhi',
    picture='img.jpg',
)








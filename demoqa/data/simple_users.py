import dataclasses

@dataclasses.dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str | None = None
    permanent_address: str | None = None

test_simple_user_1 = SimpleUser(full_name='James Bond', email='JamesBond@misix.com')
test_simple_user_2 = SimpleUser('another simple user', 'user@hg.com', 'Real address is current', 'permanent address is not the same')



from utils import create_keyboard
from types import SimpleNamespace # Create a namespace to change the dictionary from A['b'] to A.b


KEYS = SimpleNamespace(**dict(
    random_connect = 'Connect',
    settings = 'Settings'
))

KEYBOARDS = SimpleNamespace(**dict(
    # main = create_keyboard([keys['random_connect'], keys['settings']])
    main = create_keyboard([KEYS.random_connect, KEYS.settings])
))
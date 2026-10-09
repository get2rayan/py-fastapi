from slowapi import Limiter
from slowapi.util import get_remote_address

# Initialize Rate limiter using client's remote IP address
limiter = Limiter(key_func=get_remote_address, default_limits=["25/minute"])

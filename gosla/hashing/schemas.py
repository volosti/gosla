import argon2 as argon2_cffi
from passlib.hash import argon2


# explicit setting for auto update
argon2 = argon2.using(
    salt_size=argon2_cffi.DEFAULT_RANDOM_SALT_LENGTH,
    memory_cost=argon2_cffi.DEFAULT_MEMORY_COST,
    rounds=argon2_cffi.DEFAULT_TIME_COST,
    parallelism=argon2_cffi.DEFAULT_PARALLELISM,
    digest_size=argon2_cffi.DEFAULT_HASH_LENGTH,
)

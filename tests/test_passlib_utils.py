from passlib.hash import md5_crypt
from passlib_utils.schemas import argon2
from passlib_utils import __version__
from passlib_utils import PasswordHelper, PasswordMixin


def test_version():
    assert __version__ == '0.1.0'


def test_password_setting():
    model = PasswordMixin()
    model.set_password('password')
    assert model.verify_password('password') == (True, False)
    assert model.password != 'password'
    assert model.verify_password(model.password) == (False, False)


def test_argon2_updating():
    model = PasswordMixin()

    password = argon2.hash('password')
    model.password = password
    assert model.verify_password('password') == (True, False)
    assert password == model.password

    password = argon2.using(memory_cost=102000).hash('password')
    model.password = password
    assert model.verify_password('password') == (True, True)
    assert password != model.password

    password = argon2.using(time_cost=1).hash('password')
    model.password = password
    assert model.verify_password('password') == (True, True)
    assert password != model.password


def test_md5_to_argon2_migrating():
    model = PasswordMixin()
    model.password_helper = PasswordHelper([argon2, md5_crypt])

    password = md5_crypt.hash('password')
    model.password = password
    schema_name = model.password_helper.identify(model.password)
    assert schema_name == 'md5_crypt'
    assert model.verify_password('password') == (True, True)
    assert password != model.password
    schema_name = model.password_helper.identify(model.password)
    assert schema_name == 'argon2'

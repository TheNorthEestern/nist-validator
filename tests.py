from validators.nist import NISTRules
import pytest

@pytest.fixture
def ruleset():
    return NISTRules()

def test_password_too_short(ruleset):
    short_password = "123"
    assert ruleset.password_is_too_short(short_password) == True

def test_password_too_long(ruleset):
    long_password = "12345678123456781234567812345678123456781234567812345678123456789"
    assert ruleset.password_is_too_long(long_password) == True

def test_password_too_common(ruleset):
    user_password = 'common'
    common_passwords = set(['really', 'common', 'passwords'])
    assert ruleset.is_common(user_password, common_passwords) == True

def test_password_is_not_ascii(ruleset):
    user_password = '私は日本語を勉強します' 
    assert ruleset.is_ascii(user_password) == False

# test_security.py
from builtins import isinstance, str
import pytest
from app.utils.security import hash_password, verify_password

@pytest.fixture
def hashed_password():
    """Fixture to generate a hashed password."""
    password = "secure_password"
    return hash_password(password)

def test_hash_password(hashed_password):
    """Test that hashing password returns a bcrypt hashed string."""
    assert hashed_password is not None
    assert isinstance(hashed_password, str)
    assert hashed_password.startswith('$2b$')

def test_hash_password_with_different_rounds():
    """Test hashing with different cost factors."""
    password = "secure_password"
    hashed_10 = hash_password(password, rounds=10)
    hashed_12 = hash_password(password, rounds=12)
    assert hashed_10 != hashed_12, "Hashes should differ with different cost factors"

def test_verify_password_correct(hashed_password):
    """Test verifying the correct password."""
    password = "secure_password"
    assert verify_password(password, hashed_password) is True

def test_verify_password_incorrect(hashed_password):
    """Test verifying the incorrect password."""
    wrong_password = "incorrect_password"
    assert verify_password(wrong_password, hashed_password) is False

def test_verify_password_invalid_hash():
    """Test verifying a password against an invalid hash format."""
    with pytest.raises(ValueError):
        verify_password("secure_password", "invalid_hash_format")

@pytest.mark.parametrize("password", [
    "",
    " ",
    "a"*100  # Long password
])
def test_hash_password_edge_cases(password):
    """Test hashing various edge cases."""
    hashed = hash_password(password)
    assert isinstance(hashed, str) and hashed.startswith('$2b$'), "Should handle edge cases properly"

def test_verify_password_edge_cases(hashed_password):
    """Test verifying passwords with edge cases."""
    assert verify_password(" ", hashed_password) is True
    assert verify_password("not empty", hashed_password) is False

# This function tests the error handling when an internal error occurs in bcrypt
def test_hash_password_internal_error(monkeypatch):
    """Test proper error handling when an internal bcrypt error occurs."""
    def mock_bcrypt_gensalt(rounds):
        raise RuntimeError("Simulated internal error")

    monkeypatch.setattr("bcrypt.gensalt", mock_bcrypt_gensalt)
    with pytest.raises(ValueError):
        hash_password("test")

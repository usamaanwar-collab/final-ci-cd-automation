# test_gatekeeper.py
from app_logic import add_participant_to_challenge, validate_otp_format

def test_add_participant():
    # If I have 5 people and add 1, I should have 6
    assert add_participant_to_challenge(5) == 6

def test_otp_validation():
    # A 6-digit OTP should be True
    assert validate_otp_format("123456") == True
    # A 3-digit OTP should be False
    assert validate_otp_format("123") == False
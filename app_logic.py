# app_logic.py

def add_participant_to_challenge(current_count):
    # This is a simple logic: if we add a person, the count goes up by 1
    return current_count + 1

def validate_otp_format(otp):
    # Simple check: Is the OTP exactly 6 digits?
    return len(otp) == 6 and otp.isdigit()
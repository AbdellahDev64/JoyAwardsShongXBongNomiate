import hashlib
from omkar_temp_mail import TempMail
import re

def encodeToSHA256(input:str):
    encoded_input=input.encode()
    hashed_input=hashlib.sha256(encoded_input)
    return hashed_input.hexdigest()


def extractEmailOTPCode(email:str)->str:
    body = TempMail.get_body(email)
    pattern = r'(?:"(\d+)"|: ?(\d+))'
    match = re.search(pattern, body)
    extracted_code = match.group(1) or match.group(2)
    return extracted_code

def appendJOYAWARDSAccount(accessToken:str, JWToken:str)->bool:
    with open("joy_awards_accounts_nominate_shongxbong.ini","+a") as file:
        file.write(f"accessToken:'{accessToken}', JWTOKEN:'{JWToken}'\n")
        return True
    return False

import requests
import constants
import randomizer
import utils


def verifyOTP(email:str, password:str, otp:str)->dict:
    response = requests.post(constants.JOYAWARDS_CHECKAPPOTP, data={"otp":otp,"passcode":utils.encodeToSHA256(password),"username":email}, headers={"Content-Type": "application/x-www-form-urlencoded","Accept": "*/*","Accept-Encoding": "deflate, gzip","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"})
    if response.status_code == 200:
        try:
            data = response.json()
            if("access_token" in data):
                print(f"[✔] '{email}:{password}' JoyAwards account verified successfully!")
                return {"success": True, "accessToken": data["access_token"], "JWTOKEN":data["socketJwt"]}
            else:
                print("[X] Failed to verify JoyAwards account.")
        except ValueError:
            print("[X] Unable to verify the Joy Awards account.")
    else:
        print("[X] Unable to verify the Joy Awards account.")
        print(response.text)

    return {"success": False}
    


def createJoyAwardsAccount(email:str, password:str, firstName:str, lastName:str)->bool:
    
    payload = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": utils.encodeToSHA256(password),
        "acceptedTermsAndConditions": True,
        "receivesNewsLetter": False,
        "birthday": randomizer.generateRandomDateOfBirth(),
        "country": randomizer.generateRandomCountryCode()
    }
    response = requests.post(constants.JOYAWARDS_CREATEACCOUNT, data=payload)
    if response.status_code == 200:
        try:
            data = response.json()
            if(not data["error"]):
                print(f"[✔] '{email}' JoyAwards account created successfully!")
                return True
            else:
                print("[X] Failed to create JoyAwards account.")
            
        except ValueError:
            print("[X] Unable to create the Joy Awards account.")
    else:
        print("[X] Unable to create the Joy Awards account.")

    return True

def nominateContestant(contestantID: str, subcategoryId: str, bearerToken: str, contestantName: str) -> bool:
    payload = {
        "contestant": contestantID,
        "subcategoryId": subcategoryId
    }
    headers = {
        "Authorization": bearerToken,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    response = requests.post(constants.JOYAWARDS_NOMINATE, json=payload, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            if data["_id"]:
                print(f"[✔] Contestant '{contestantName}' nominated successfully!")
                return True
            else:
                print("[X] Failed to nominate contestant. API returned an error.")
        except ValueError:
            print("[X] Can't nominate contestant(Reason: Invalid response format from the server.)")
    else:
        print(f"[X] Failed to nominate contestant.")
    
    return False
    
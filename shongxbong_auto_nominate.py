import joyAwardsAPI, time,randomizer, utils


def prepareAccount()->dict:
    try:
        fullName=randomizer.getRandomFullName()
        email:str =randomizer.generateRandomEmail(fullName["firstName"], fullName["lastName"])
        password:str=randomizer.generatePassword(fullName["firstName"], fullName["lastName"])
        created:bool=joyAwardsAPI.createJoyAwardsAccount(email=email,password=password,firstName=fullName["firstName"],lastName=fullName["lastName"])
        time.sleep(2)
        otp:str=utils.extractEmailOTPCode(email=email)
        response=joyAwardsAPI.verifyOTP(email=email,password=password,otp=otp)
        return {"success": created and response["success"], "bearerToken": response["accessToken"] if "accessToken" in response else None, "jwtoken": response["JWTOKEN"] if "JWTOKEN" in response else None}
    except:
        return {"success":False}

def nominateShongXBong(accessToken:str)->bool:
    SHONGXBONG_CONTESTANTID="673776146b0da3a2c6b6012a"
    SHONGXBONG_SUBCATEGORYID="614482a10684091e660624ea"
    return joyAwardsAPI.nominateContestant(SHONGXBONG_CONTESTANTID, SHONGXBONG_SUBCATEGORYID, accessToken,"SHoNgxBоNg")

def main():
    nominated_count:int=0
    with open("joy_awards_accounts_nominate_shongxbong.ini", "r") as file:
        nominated_count = sum(1 for line in file) +1
    while(True):
        account=None
        try:
            account:bool=prepareAccount()
        except AssertionError:
            continue
        if(account["success"]):
            nominated:bool=nominateShongXBong(account["bearerToken"])
            if(nominated): 
                nominated_count+=1
                utils.appendJOYAWARDSAccount(account["bearerToken"],account["jwtoken"])
        print(f"=====================< {nominated_count} >=====================")


main()
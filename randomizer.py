import random
from datetime import datetime, timedelta
from omkar_temp_mail import TempMail
import names

def generateRandomCountryCode():
    return ["DZ", "LY", "TN", "MR", "SD", "EG", "SA", "QA", "BH", "KW", "MA", "AE", "OM", "YE", "JO", "PS", "LB", "SY", "IQ", "SO", "KM"][random.randint(0,20)]

def generateRandomDateOfBirth(min_age=17, max_age=38):
    today = datetime.today()
    
    max_birth_year = today.year - min_age
    min_birth_year = today.year - max_age
    
    random_year = random.randint(min_birth_year, max_birth_year)
    random_month = random.randint(1, 12)

    last_day_of_month = (datetime(random_year, random_month, 1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    random_day = random.randint(1, last_day_of_month.day)
    random_dob = datetime(random_year, random_month, random_day).strftime("%m-%d-%Y")
    return random_dob

def generateRandomEmail(firstName:str, lastName:str):
    domains=TempMail.get_domains()
    email:str = f"{firstName.lower()}{random.randint(10,99)}.{lastName.lower()}{random.randint(10,99)}@"+domains[random.randint(0,len(domains)-1)]
    return email

def getRandomFullName():
    first_name:str = names.get_first_name(gender='female' if random.randint(0,1) else 'male')
    last_name:str = names.get_last_name()
    return {"firstName": first_name, "lastName": last_name}

def generatePassword(firstName: str, lastName: str) -> str:
    shuffled_name = ''.join(random.sample(firstName + lastName, len(firstName + lastName)))
    random_number = str(random.randint(10, 99))
    special_chars = random.choices("!@#$%^&*()", k=2)
    mixed_case = ''.join(random.choice([c.upper(), c.lower()]) for c in shuffled_name[:6])
    password:str = mixed_case + random_number + ''.join(special_chars)
    password = ''.join(random.sample(password, len(password)))
    return password
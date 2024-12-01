# Mass Nomination of ShongXBong for JoyAwards 🏆

This Python script automates the process of nominating ShongXBong in the JoyAwards app, helping him secure the prize because he's the only person who truly deserves it.

## Who is ShongXBong? 👑
![ShongXBong](https://github.com/AbdellahDev64/Alaa-Engine-Edited/blob/main/SHoNgxB%D0%BENg.png?raw=true)

**ShongXBong**, also known as **Ahmed Al-Qahtani**, is a prominent Saudi influencer and YouTuber with over **13 million followers**. He creates engaging content primarily focused on **gaming** and **e-sports**. His vibrant personality and dedication to his craft have earned him several accolades, including **"Best Streamer"** and **"Best Content Creator"** awards from **2021** to **2023**. Most notably, he won the **"Favourite Male Influencer"** award at the **2024 Joy Awards**, a prestigious event held in Riyadh that celebrates the global entertainment industry.

His success at the JoyAwards was a significant milestone, further solidifying his influence within the gaming and entertainment sectors. Fans and supporters are now rallying behind him to ensure he secures **another win in 2025**.
## Tutorial
[![tuto](https://img.youtube.com/vi/F6Vu_xMcu-A/0.jpg)](https://www.youtube.com/watch?v=F6Vu_xMcu-A)

## Installation 💻
In the terminal:
```bash
pip install omkar-temp-mail names requests
git clone https://github.com/AbdellahDev64/JoyAwardsShongXBongNominate.git
```
## Usage ▶️
Navigate to the installation directory, then simply run:
```python
python shongxbong_auto_nominate.py
```
### **That's it :)** 

![How it Looks From Inside](https://github.com/AbdellahDev64/Alaa-Engine-Edited/blob/main/2024-11-29-14-55-25-_online-video-cutter.com_.gif?raw=true)


You will notice a new file is created called **joy_awards_accounts_nominate_shongxbong.ini**, which contains all accounts that nominate ShongXBong in the JoyAwards in the following format:
```text
accessToken:'Bearer XXXXXXXXXXXXXXXXX', JWTOKEN:'XXXXXXXXXXXXXXXXXX', PASSWORD:'XXXXXXXXXXXX'

// Meaning:
accessToken: The Bearer Token for the JoyAwards session (valid for 120h before expiration)
JWTOKEN: Can be decoded at https://jwt.io/ to retrieve all account data, 
         such as email.
PASSWORD: JoyAwards account's password.
```
![JOYAWARDS_JWTOKEN](https://github.com/AbdellahDev64/Alaa-Engine-Edited/blob/main/Acc.png?raw=true)

## Validation ✅
You can install the **JoyAwards App** from the **Google Play Store** or **App Store**. Use the same email and password, and you'll see that you successfully logged in and nominated ShongXBong.

## How it works? ⚙️
- Generates a random first name, last name, country code, date of birth, and valid email address.
- Uses the JoyAwards web API to create an account with these details.
- A verification code is sent to the email, which is received and extracted from the message.
- Verifies the account using the extracted code.
- Uses the JoyAwards API again to nominate ShongXBong as a contestant.

**-> That's it !!**

## 🛠 Built With
![Static Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## Hi, I'm Abdellah Elidrissi! 👋
Passionate developer and student with a diverse skill set that spans across various domains. From Web Development utilizing technologies like Asp.net Core MVC, Node.js, HTML, CSS, JavaScript, and React, to Android Development with expertise in Java and Flutter, I've ventured into Desktop Development using WinForms in C# and even dived into the world of Games Development, specializing in Unreal Engine. Additionally, I have a knack for 3D Design, leveraging tools like Blender to bring creative ideas to life.

I embarked on this journey in the world of programming at the age of 13, and my trajectory has been a fascinating evolution, starting from desktop applications to conquering the realms of Android, Games, and finally Web Development. Currently, I'm studying at ENSA MARRAKECH in Morocco.

With a genuine love for programming, I find joy in turning concepts into functional and aesthetically pleasing applications. I'm excited to see what challenges and innovations lie ahead in this ever-evolving field.

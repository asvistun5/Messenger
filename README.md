# Проєкт Соціальна мережа / Social Network Project

---
## У розробці проекту приймали участь / Participated in the development of the project :
1. [Скрипник Миколай](https://github.com/Nikolay2012) - Керівник проекту / Project manager.
2. [Левковський Дмитро](https://github.com/Levkivskiydmitro) - Тімлід команди / Team leader.
3. [Шматько Дмитро](https://github.com/DimaShmatko999) - Працівник команди / Team worker.
4. [Свистун Артем](https://github.com/asvistun5) - Працівник команди / Team worker.

---
## Зміст / Content
1. [Назва проєкту](#назва-проєкту) / [Project name](#project-name)
2. [Зображення-превью проєкту](#зображення-превью-проєкту) / [Project Preview Image](#project-preview-image)
3. [Мета проєкту та цільова аудиторія](#мета-проєкту-та-цільова-аудиторія) / 
4. [Зміст README.md](#зміст-readmemd) / [Table of contents README.md](#table-of-contents-readmemd)
5. [Діаграма-структура проєкту](#діаграма-структура-проєкту) / [Project Structure Diagram](#project-structure-diagram)
6. [Розгортання проєкту на локальному ПК](#розгортання-проєкту-на-локальному-пк) / [Deploying a project on a local PC](#deploying-a-project-on-a-local-pc)
    - [Windows](#windows)
    - [Mac](#mac)
7. [Налаштування віртуального оточення](#налаштування-віртуального-оточення) / [Virtual Environment Settings](#virtual-environment-settings)
    - [Windows](#windows-1)
    - [Mac](#mac-1)
8. [Запуск проєкту](#запуск-проєкту) / [Start a project](#start-a-project)
    - [Windows](#windows-2)
    - [Mac](#mac-2)
9. [Особливості розробки](#особливості-розробки) / [Development Features](#development-features)
    - [Робота з зображеннями](#робота-з-зображеннями) / [Working with images](#working-with-images)
    - [Робота з веб-сокетами](#робота-з-веб-сокетами) / [Working with web sockets](#working-with-web-sockets)
    - [Принцип роботи постів, альбомів, налаштувань, чатів](#принцип-роботи-постів-альбомів-налаштувань-чатів) / [How posts, albums, settings, chats work](#how-posts-albums-settings-chats-work)
    - [Принцип роботи реєстрації та авторизації](#принцип-роботи-реєстрації-та-авторизації) / [How registration and authorization work](#how-registration-and-authorization-work)
    - [Додаток друзів та додавання користувачів](#додаток-друзів-та-додавання-користувачів) / [Friends and Users App](#friends-and-users-app)
10. [Висновок](#висновок) / 
    [Conclusion](#conclusion)

---

## Назва проєкту / Project name
Соціальна мережа для обміну контентом, чатами та створенням друзів. / A social network for sharing content, chatting, and making friends.

---

## Зображення-превью проєкту / Project preview image
![Social Network Preview]()

---

## Мета проєкту та цільова аудиторія / Project goal and target audience
Проєкт створений для того, щоб забезпечити користувачів платформою для спілкування, обміну медіа, створення альбомів, чатів та управління друзями. Основною метою є створення інтерактивної та зручної платформи для обміну інформацією між користувачами. / The project was created to provide users with a platform for communication, media sharing, album creation, chat, and friend management. The main goal is to create an interactive and convenient platform for information exchange between users.

Проєкт буде корисним для тих, хто шукає: / The project will be useful for those looking for:
- Платформу для спілкування та зберігання контенту. / A platform for communication and content storage.
- Просту систему для створення постів, альбомів та спілкування через чат. / A simple system for creating posts, albums, and communicating via chat.
- Можливість взаємодії з друзями та іншими користувачами через веб-сокети. / Ability to interact with friends and other users via web sockets.

---

## Зміст README.md / Content README.md
У цьому файлі детально описано, як розгорнути проєкт на локальному ПК, налаштувати віртуальне оточення, запустити проект, а також розглянуто основні функції, такі як робота з зображеннями, веб-сокетами, AJAX і багато іншого. / This file details how to deploy a project to a local PC, set up a virtual environment, run the project, and also covers basic features such as working with images, web sockets, AJAX, and more.

---

## Діаграма-структура проєкту / Project structure diagram
![Project Structure Diagram](link_to_project_structure_diagram.jpg)

---

## Розгортання проєкту на локальному ПК / Deploying a project on a local PC
### Windows
1. Клонуйте репозиторій на свій комп'ютер: / Download the project from GitHub:

   ```bash
   git clone https://github.com/your-username/social-network.git

2. Перейдіть до папки проєкту: / Go to the project folder:

   ```bash
   cd social-network

3. Встановіть залежності: / Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Налаштуйте базу даних (якщо необхідно): / Configure the database:

   ```bash
   python manage.py migrate

5. Запустіть сервер: / Start the server:

   ```bash
   python manage.py runserver

6. Відкрийте браузер і перейдіть за адресою http://127.0.0.1:8000 / Open a browser and go to http://127.0.0.1:8000

### Mac
1. Завантажте проєкт з GitHub: / Download the project from GitHub:

   ```bash
   git clone https://github.com/username/social-network.git

2. Перейдіть до папки проєкту: / Go to the project folder:

   ```bash
   cd social-network

3. Встановіть залежності: / Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Налаштуйте базу даних: / Configure the database:

   ```bash
   python manage.py migrate

5. Запустіть сервер: / Start the server:

   ```bash
   python manage.py runserver

6. Відкрийте браузер і перейдіть за адресою http://127.0.0.1:8000 / Open a browser and go to http://127.0.0.1:8000

---

## Налаштування віртуального оточення / Setting up a virtual environment
### Windows
1. Встановіть Python (якщо не встановлений). / Install Python (if not installed).

2. Створіть віртуальне оточення: / Create a virtual environment:

   ```bash
   python -m venv venv

3. Активуйте віртуальне оточення: / Activate the virtual environment:

   ```bash
   .\venv\Scripts\activate

4. Встановіть залежності: / Install dependencies:

   ```bash
   pip install -r requirements.txt

### Mac
1. Встановіть Python (якщо не встановлений). / Install Python (if not installed).

2. Створіть віртуальне оточення: / Create a virtual environment:

   ```bash
   python3 -m venv venv

3. Активуйте віртуальне оточення: / Activate the virtual environment:

   ```bash
   source venv/bin/activate

4. Встановіть залежності: / Install dependencies:

   ```bash
   pip install -r requirements.txt

---

## Запуск проєкту / Launch of the project
### Windows
1. Переконайтеся, що віртуальне оточення активоване. / Make sure the virtual environment is activated.

2. Запустіть сервер: / Start the server

   ```bash
   python manage.py runserver

3. Відкрийте браузер і перейдіть за адресою http://127.0.0.1:8000 / Open a browser and go to http://127.0.0.1:8000

### Mac
1. Переконайтеся, що віртуальне оточення активоване. / Make sure the virtual environment is activated.

2. Запустіть сервер: / Start the server

   ```bash
   python manage.py runserver

3. Відкрийте браузер і перейдіть за адресою http://127.0.0.1:8000 / Open a browser and go to http://127.0.0.1:8000

---

## Особливості розробки / Development features

### Робота з зображеннями / Working with images
У проєкті реалізована можливість завантаження та обробки зображень, які користувачі можуть використовувати для своїх профілів або публікацій. / The project implements the ability to upload and process images that users can use for their profiles or publications.

### Робота з веб-сокетами / Working with web sockets
Для реалізації чатів та миттєвих повідомлень використовується бібліотека Django Channels, яка забезпечує з'єднання через веб-сокети. / To implement chats and instant messages, the Django Channels library is used, which provides connections via web sockets.

### Принцип роботи постів, альбомів, налаштувань, чатів / How posts, albums, settings, chats work
Пости: Користувачі можуть створювати пости, додавати теги, а також реагувати на пости інших користувачів. / Posts: Users can create posts, add tags, and react to other users' posts.

Альбоми: Користувачі можуть створювати альбоми для зберігання фотографій. / Albums: Users can create albums to store photos.

Налаштування: Користувачі можуть змінювати персональні налаштування профілю. / Settings: Users can change their personal profile settings.

Чати: Доступні як індивідуальні чати, так і групові чати. Використовується AJAX для асинхронних оновлень. / Chats: Both individual and group chats are available. AJAX is used for asynchronous updates.

### Принцип роботи реєстрації та авторизації / How registration and authorization work
Процес реєстрації користувача включає перевірку email, пароль та введення особистих даних. Авторизація здійснюється через сесію. / The user registration process includes email verification, password verification, and entering personal data. Authorization is done through a session.

### Додаток друзів / Friends app
Користувачі можуть додавати інших користувачів у список друзів для зручнішої комунікації. / Users can add other users to their friends list for more convenient communication.

---

## Висновок / Conclusion
Проєкт Social Network був корисним як для практики роботи з різноманітними веб-технологіями, так і для розуміння механізмів, які стоять за соціальними мережами. Під час розробки я набув важливого досвіду у використанні Django, роботі з базами даних, а також у розробці асинхронних функцій для чатів і миттєвих повідомлень. Мені вдалося глибше зрозуміти як працюють AJAX-запити та веб-сокети, що дозволило зробити спілкування в додатку більш динамічним. Крім того, реалізація підтримки зображень дозволила покращити взаємодію користувачів з платформою, адже фотографії є важливою частиною соціальної взаємодії. / The Social Network project was useful both for practicing working with various web technologies and for understanding the mechanisms behind social networks. During the development, I gained important experience in using Django, working with databases, as well as in developing asynchronous functions for chats and instant messages. I was able to understand in more depth how AJAX requests and web sockets work, which allowed me to make communication in the application more dynamic. In addition, the implementation of image support allowed me to improve user interaction with the platform, since photos are an important part of social interaction.

Цей проєкт також став корисним для покращення моїх навичок роботи з фронтендом, зокрема в області створення інтерактивних інтерфейсів для роботи з даними. Використання таких технологій як AJAX і WebSockets значно покращило швидкість і зручність. / This project was also useful for improving my frontend skills, particularly in the area of ​​creating interactive interfaces for working with data. Using technologies like AJAX and WebSockets significantly improved speed and usability.

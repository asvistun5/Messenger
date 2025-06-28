# Project "Messanger — Social network" 
<span style="color: gray; font-size: 24px;">| Проєкт "Messanger — Соціальна мережа"</span>

![Image](http://bit.ly/4epMEbb)

# Purpose of the Project 
<span style="color: gray; font-size: 22px;">| Мета створення проєкту</span>

For your convenience, a convenient interface will be available for registration, authorization, create posts, add friends, chat, settings, and much more.  
*Для вашої зручності буде доступний зручний інтерфейс для реєстрації, авторизації, створення постів, додавання друзів, чатів, налаштувань та багато іншого.*

## У розробці проекту приймали участь / Participated in the development of the project :
1. [Левківський Дмитро](https://github.com/Levkivskiydmitro) - Тімлід команди / Team leader.
2. [Свистун Артем](https://github.com/asvistun5) - Працівник команди / Team worker.
3. [Шматько Дмитро](https://github.com/DimaShmatko999) - Працівник команди / Team worker.

# Project structure
<span style="color: gray; font-size: 22px;">| Структура проекту</span>

![Image](http://bit.ly/4epMEbb)

## Launching a project on a local PC 
<span style="color: gray; font-size: 20px;">| Розгортання проєкту на локальному ПК</span>

### 1. Завантаження проекту
Відкрийте Git bash термінал та пропишіть команду для копіювання проекту на ваш ПК
```bash
git clone https://github.com/asvistun5/Messenger
```
Після цього, перейдіть в папку проєкту за допомогою команди:
```bash
cd Messenger
```

#### Або скористуйтесь кнопкою 'Code' та завантажте проєкт

### 2. Налаштування віртуального оточення
Віртуальне оточення допомагає ізолювати залежності вашого проекту.
#### Для Windows:
Створіть віртуальне оточення за допомогою команди:
```powershell
python -m venv venv
```
Та активуйте оточення за допомогою команди:
```powershell
.\venv\Scripts\activate
```

---

#### Для Mac:
Створіть віртуальне оточення за допомогою команди:
```bash
python3 -m venv venv
```
Та активуйте оточення за допомогою команди:
```bash
source venv/bin/activate
```

### 3. Встановлення залежностей:
Для цього пропишіть цю команду:
```bash
pip install -r requirements.txt
```

## Launch of the project
<span style="color: gray; font-size: 20px;">| Запуск проєкту</span>

### 1. Переконайтесь, що у вас активоване віртуальне оточення
### 2. Налаштування бази даних:
#### Для Windows:
Вам потрібно створити базу даних та застосувати міграції:
```bash
python manage.py migrate
```

#### Для Mac:
Вам потрібно створити базу даних та застосувати міграції:
python3 manage.py migrate

### 3. Запуск серверу:
#### Для Windows:
```bash
python manage.py runserver
```

#### Для Mac:
```bash
python3 manage.py runserver
```

## Conclusion
<span style="color: gray; font-size: 20px;">| Підсумок:</span>
#### Thanks to this project, we got a lot of experience, learned how to write in the Django framework, and improved our skills in writing HTML and CSS files. We also improved our work with GitHub, and learned how to work on our own branch.  |  Завдяки цьому проекту ми отримали великий опит, навчилися написанню у фреймворку Django та покращили навички написання HTML та CSS файлів. Також покращили працю з GitHub, и навчилися працювати кожен над своею віткою.

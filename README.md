# life-manager
**Software to keep track of your daily habits, help you achieve goals, keep notes, and generally organize your life.**

- Tracks up to 9 numbers and up to 9 checks every day, all customizable (e.g. weight, money spent, exercise completed, hygiene-related things, etc)
- The interface is also customizable, with customizable widgets, colors, method of editing each value.
- Has a calendar where you can see stats for and edit each day.
- You can set reminders for each day and see reminders from previous days
- You can have multiple databases
- The interface is available in both English and Bulgarian
- The entire program is just one Python script
- (WIP) Can show charts and visualizations of the trends throughout a period of time
- (WIP) Can add new elements and edit the style of already created databases

**Required modules: pygame  
Tested under pygame 2.0.1 (SDL 2.0.14, Python 3.9.2)**

**Important!**
- While the program can run under any common environment, it's designed for **touchscreen devices with 1024x600 resolution**.
- Specifically - cheap 7" Android tablet (the ones that go for $50). A Raspberry Pi with a touch display will also work.
- You can run the program under other resolutions with a choice of how to scale it to your display.
- The program requires the Calibri font (**calibri.ttf**) in the same directory, which it will download automatically if you have Internet connection and the requests module.
- You can set the program to load a database automatically by typing the command setauto in the "Reminders" field. Type stopauto if you want to disable it.

**How to run on Android:**
1. Download Pydroid 3 from Google Play Store
2. Go to PIP in the menu and install the pygame library
3. Open main.py file in the repository and copy the entire contents
4. Paste it into the Pydroid IDE
5. Run the program, choose language and anti-aliasing options
6. You will see the directory where you should place the font file,
7. Press OK to go to the download page
8. Download the font file (calibri.ttf) from the repository and place it in the directory
9. Run the program again

You can skip steps 6 - 9 by just installing the requests library, then the program will download the font file automatically.

------------
български

------------

**Софтуер, който Ви следи ежедневните навици, помага да постигнете цели, правите бележки, и като цяло Ви организира живота.**
- Следи до 9 числени стойности и до 9 отметки всеки ден, всичките персонализирани (примерно тегло, похарчени пари, направени упражнения, неща свързани с хигиена, т.н.)
- Интефейса също може да се персонализира, с персонализирани widget-и, цветове, методи за промяна на всяка стойност.
- Има календар, където можете да видите статистика за всеки ден и да го редактирате.
- Можете да пишете бележки за всеки ден и да виждате бележките от изминали дни
- Може да имате няколко бази данни.
- Интерфейсът е наличен на български и на английски
- Цялата програма е във един Python скрипт
- (ВПО) Може да показва диаграми и визуализации на тендециите в период от време
- (ВПО) Може да добавяте нови елементи и да променяте стила на вече създадени бази данни

**Нужни модули: pygame  
Тествано под pygame 2.0.1 (SDL 2.0.14, Python 3.9.2)**

**Важно!**
- Програмата може да работи под всякакви често срещани работни среди, но е създадена за **тъчскрийн устройства с 1024х600 резолюция**.
- По-точно - евтини 7" Андроид таблети (тези под 100лв). Raspberry Pi със тъч дисплей също работи.
- Можете да пуснете програмата под други резолюции и да изберете как да бъде оразмерена.
- Програмата изисква шрифтът Calibri (**calibri.ttf**) в същата директория. Ще бъде изтеглен автоматично ако имате интернет и модулът requests
- Можете да зададете на програмата автоматично да отваря база данни като напишете командата setauto в полето Бележки. Напишете stopauto за да спрете тази функция.

**Как да пуснете от Android:**
1. Изтеглете Pydroid 3 от Google Play Store
2. Отворете PIP в менюто и инсталирайте pygame библиотеката
3. Отворете main.py файлът в GitHub и копирайте цялото съдържание
4. Поставете го в Pydroid IDE
5. Пуснете програмата, изберете настройки за език и за изглаждане
6. Ще видите директорията, в която трябва да поставите файлът за шрифта
7. Натиснете ОК и ще бъдете пренасочени към страницата за изтегляне
8. Изтеглете файлът за шрифта (calibri.ttf) от страницата и го поставете в директорията
9. Пуснете програмата отново

Може да пропуснете стъпки 6 - 9 ако просто инсталирате библиотеката requests, тогава програмата сама ще изтегли файла.

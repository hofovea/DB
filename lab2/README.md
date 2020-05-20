# Лабораторна робота 2: Практичне використання сервера Redis

Було використано SET для представлення користувачів системи, де ключем є роль користувача: власник, адміністратор та звичайних користувач.
Звичайний користувач може надсилати повідомлення та переглядати власну скриньку. Адміністратор має можливості Користувача 
та додатково може переглядати спамерів та дивитись скільки користувачів знаходяться онлайн. 
Власник має всі можливості Адміністратора, але додатково може змінювати ролі вже наявних користувачів.
Перевага SET у тому, що пошук даних у ній здійснюється за константний час, 
що є дуже зручним при роботі з основними операціями користувачів системи: зміна/перевірка ролей, отримання даних про користувачів. 

ZSET було використано для реалізації списку спамерів, окільки він берігає дані відсортованими по певному ключу.

HASH використовувався для збереження повідомлнь, адже у цій СД набори зберігаються як ключ-значення.
Ключ генерувався за допомогою бібліотеки hashlib.

Pub/Sub був використаний для реалізації Журналу Активностей, у якому відображаються повідомлення про спам та підключення/відключення користувачів.

Для черги надсилання повідомлень та відображення користувачу його власних вхідних повідомлень використано LIST з метою збереження порядку даних.
Ще одною перевагою LIST у даному випадку є те, що вилучення даних з кінця та додавання їх на початок відбувається за сталий час.

## Результати роботи
Робота журналу активностей та можливості користувача в ролі Власника
![1](screenshots/1)
___
Mожливості користувача в ролі Адміністратора
![2](screenshots/2)
___
Можливості користувача в ролі Користувача та процес зміни ролі Користувач на Адміністратор
![3](screenshots/3)
___
Можливості користувача admin після зміни ролі Адміністратор на Користувач
![4](screenshots/4)
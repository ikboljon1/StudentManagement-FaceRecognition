# Система управления учета посещаемости студентов с распознаванием лиц
StudentManagement-FaceRecognition - это удобное приложение для автоматизации учета посещаемости студентов в учебных заведениях. Его основные преимущества:
- Простота внедрения - не требует сложной настройки или дополнительного оборудования. Работает через веб-камеру.
- Точность распознавания - используются передовые алгоритмы компьютерного зрения для надежной идентификации лиц.
- Удобный интерфейс - интуитивно понятное для пользователя взаимодействие.
- Хранение данных - все сведения о посещаемости надежно сохраняются в базе данных.
- Аналитика - отслеживание динамики посещаемости каждого студента.
## Как это работает:

<img src="https://github.com/ikboljon1/StudentManagement-FaceRecognition/assets/63257726/31b7af90-8bb2-482c-b905-2f485899f984" width="450" height="250">

<img src="https://github.com/ikboljon1/StudentManagement-FaceRecognition/assets/63257726/4776ab81-9e02-40e9-a6e3-f99a7063c9c8" width="450" height="250">

<img src="https://github.com/ikboljon1/StudentManagement-FaceRecognition/assets/63257726/1d1cc921-f784-4f17-8a28-6eba5e3a5ac5" width="450" height="250">

## Используемые технологии:
- Язык программирования: ![Python](https://img.shields.io/badge/python-3670A0?&logo=python&logoColor=ffdd54)
- Библиотеки: 	![Tkinter](https://img.shields.io/badge/Tkinter-003545?&logo=Tkinter&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?&logo=opencv&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?&logo=numpy&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQConnector-%2300f.svg?&logo=mysql&logoColor=white)
- База данных: ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?&logo=mysql&logoColor=white)

## Установка:
1. Клонируйте репозиторий:
  ```
  git clone https://github.com/ikboljon1/StudentManagement-FaceRecognition.git
  ```
2. Установите необходимые библиотеки:
  ```
  pip install opencv-python numpy mysql-connector-python
  ```
3.  Создайте базу данных MySQL и настройте подключение.Для этого нужно:
- Установить и настроить сервер MySQL.
- Создать базу данных face_recognition.
- Находите часть mysql.connector во всех файлах, таких как `Student`, `Train`, `Face_Recognition`, `Attendance`.
```conn = mysql.connector.connect(username='root', password='новый пароль',host='localhost',database='face_recognition',port=3306)```
В них меняйте пароль `password='новый пароль'`
4. Извлекайте `data_img.rar` в архив
5.  Запустите приложение командой:
  ```
  python main.py
  ```
## Использование:
- Добавляйте студентов в разделе Student Panel
- Делайте фотографии лиц каждого студента перед камерой
- Обучайте классификатор на собранных образцах лиц с помощью кнопки Train
- Затем запускайте распознавание студентов кнопкой Face Detection
- Распознанные студенты будут записываться в attendance panel

В целом, это приложение позволит вам автоматизировать процесс учета посещаемости студентов. Его можно настраивать и дополнять по своему усмотрению.




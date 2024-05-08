htmlAdmin = """<!DOCTYPE html>
<html>

<head>
    <title>Chat</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #9cad82;
            /* Светло-зелёный фон */
            color: #006400;
            /* Тёмно-зелёный цвет текста */
            margin: 0;
            padding: 20px;
        }

        h1 {
            color: #000;
        }

        .wrapper {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        #echoSection,
        .buttonsContainer {
            background-color: #F5FFFA;
            /* Пастельный фон контейнеров */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 128, 0, 0.3);
            /* Тень для контейнеров */
        }

        .buttonsContainer button,
        #echoSection button {
            background-color: #a2dda2;
            /* Зелёные кнопки */
            color: #FFFFFF;
            /* Белый текст кнопок */
            border: none;
            margin-bottom: 10px;
            /* Отступы между кнопками */
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
            /* Плавный эффект при наведении */
        }

        .buttonsContainer button:hover,
        #echoSection button:hover {
            background-color: #c5d1b7da;
            /* Затемнённый зелёный при наведении */
        }

        input[type="number"],
        input[type="text"] {
            margin-bottom: 20px;
            /* Отступ от поля ввода до кнопок */
            border-radius: 5px;
            border: 1px solid #8FBC8F;
            /* Граница с закруглёнными углами */
            width: 100%;
            /* Ширина поля ввода */
        }

        ul#messages {
            list-style-type: none;
            padding-left: 0;
        }
    </style>
</head>

<body>
    <h1>Панель администратора Petto</h1>
    <div class="wrapper">
        <div class="buttonsContainer">
            <input type="number" id="userID" placeholder="Введите id пользователя" autocomplete="off" />
            <button onclick="sendHashUserQuery()">Хэш пароля пользователя</button>
            <button onclick="sendUserWeightQuery()">Место, занимаемое пользователем на диске</button>
            <button onclick="sendUserRequest()">Получить пользователя по id</button>
            <button onclick="sendCountUsers()">Количество зарегистрированных пользователей</button>

            <input type="text" id="echoText" placeholder="Введите строку" autocomplete="off" />
            <button onclick="sendEcho()">Отправить Эхо</button>
        </div>
    </div>
    <div>
        <ul id="messages"></ul>
    </div>


    <script>
        // Ваш javascript код останется без изменений
        var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function (event) {
            var messages = document.getElementById('messages');
            var message = document.createElement('li');
            var content = document.createTextNode(event.data);
            message.appendChild(content);
            messages.appendChild(message);
        };

        function sendHashUserQuery() {
            var idInput = document.getElementById("userID");
            ws.send("get_hash_user:" + idInput.value);
        }

        function sendCountUsers() {
            ws.send('sendAnother');
        }

        function sendEcho() {
            var echoInput = document.getElementById("echoText");
            ws.send("getEcho:" + echoInput.value);
        }

        function sendUserRequest() {
            var idInput = document.getElementById("userID");
            ws.send("get_user_data:" + idInput.value);
        }

        function sendUserWeightQuery() {
            var idInput = document.getElementById("userID");
            ws.send("user_weight:" + idInput.value);
        }
    </script>
</body>

</html>
"""

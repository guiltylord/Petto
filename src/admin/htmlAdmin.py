htmlAdmin = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
        <style>
            .wrapper {
                display: flex;
                justify-content: space-between;
            }
            #echoSection {
                align-self: flex-start;
            }
        </style>
    </head>
    <body>
        <h1>Панель администратора Petto</h1>
        <div class="wrapper">
        <div>
            <input type="number" id="userID" placeholder="Введите id user" autocomplete="off"/>
            <div>
                <button onclick="sendHashUserQuery()">Хэш пароля юзера</button>
                <button onclick="sendUserWeightQuery()">Место, занимаемое юзером на диске</button> 
                <button onclick="sendUserRequest()">Получить пользователя по id</button>
            </div>
            <button onclick="sendCountUsers()">Количество зарегистрированных пользователей</button>
        </div>
        <div id="echoSection">
            <input type="text" id="echoText" placeholder="Введите строку" autocomplete="off"/>
            <button onclick="sendEcho()">Отправить Эхо</button>
        </div>
        </div>

        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('li');
                var content = document.createTextNode(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            };

            //Хэш пароля юзера
            function sendHashUserQuery() {
                var idInput = document.getElementById("userID");
                ws.send("get_hash_user:" + idInput.value); // Отправляем команду с данными
            }

            //Количество зарегистрированных пользователей
            function sendCountUsers() {
                ws.send('sendAnother');
            }

            //'Эхо'
            function sendEcho() {
                var echoInput = document.getElementById("echoText");
                ws.send("getEcho:" + echoInput.value); // Отправляем команду с данными
            }

            //Получить пользователя
            function sendUserRequest() {
                var idInput = document.getElementById("userID");
                ws.send("get_user_data:" + idInput.value); // Отправляем команду с данными
            }

            //Место, занимаемое юзером на диске
            function sendUserWeightQuery() {
                var idInput = document.getElementById("userID");
                ws.send("user_weight:" + idInput.value); // Отправляем команду с данными
            }
        </script>
    </body>
</html>
"""

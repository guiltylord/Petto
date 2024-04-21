htmlAdmin = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        
        <input type="number" id="userID" placeholder="Введите id user" autocomplete="off"/>
        
        <button onclick="sendHashUserQuery()">Хэш пароля юзера</button>
        <button onclick="sendUserWeightQuery()">Место, занимаемое юзером на диске</button>
        <button onclick="sendCountUsers()">Количество зарегистрированных пользователей</button>
        <button onclick="sendUserRequest()">Получить пользователя по id</button>
        
        <input type="text" id="echoText" placeholder="Введите строку" autocomplete="off"/>
        <button onclick="sendEcho()">Отправить Эхо</button>

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

            function sendHashUserQuery() {
                var idInput = document.getElementById("userID");
                ws.send("get_hash_user:" + idInput.value); // Отправляем команду с данными
            }

            function sendCountUsers() {
                ws.send('sendAnother');
            }

            //'Эхо'
            function sendEcho() {
                var echoInput = document.getElementById("echoText");
                ws.send("getEcho:" + echoInput.value); // Отправляем команду с данными
            }
            
            function sendUserRequest() {
                var idInput = document.getElementById("userID");
                ws.send("get_user_data:" + idInput.value); // Отправляем команду с данными
                idInput.value = '';
            }
            
            function sendUserWeightQuery() {
                var idInput = document.getElementById("userID");
                ws.send("user_weight:" + idInput.value); // Отправляем команду с данными
                idInput.value = '';
            }


        </script>
    </body>
</html>
"""

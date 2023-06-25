const roomId = JSON.parse(
    document.getElementById('room-uuid').textContent
);

const requestUser = JSON.parse(
    document.getElementById('request-user-id').textContent
);

const url = 'wss://' + window.location.host +
    '/ws/chat/room/' + roomId + '/';
const chatSocket = new WebSocket(url);

const chat = document.getElementById('chat');
chat.parentNode.scrollTop = chat.scrollHeight;

chatSocket.onmessage = function (event) {
    const data = JSON.parse(event.data);

    const dateOptions = {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true,
        day: 'numeric',
        month: 'long',
        year: 'numeric',
    };
    const datetime = new Date(data.datetime).toLocaleString('en', dateOptions);
    const isMe = data.user_id === requestUser;
    const source1 = isMe ? '' : 'text-right';
    const source2 = isMe ? 'my-message' : 'other-message float-right';
    const name = isMe ? 'Me' : data.username;

    chat.innerHTML += '<li class="clearfix">' +
                            '<div class="message-data ' + source1 + '">' +
                                '<span class="message-data-time">' + datetime + '</span>' +
                            '</div>' +
                            '<div class="message '+ source2 +'">' +
                                data.message +
                            '</div>' +
                        '</li>';

    chat.parentNode.scrollTop = chat.scrollHeight;
    // window.scrollTo(0, chat.scrollHeight);
};

chatSocket.onclose = function (event) {
    console.error('Chat socket closed unexpectedly');
};

const input = document.getElementById('chat-message-input');
const submitButton = document.getElementById('chat-message-submit');

submitButton.addEventListener('click', function (event) {
    const message = input.value;

    if (message !== '') {
        // send message in JSON format
        chatSocket.send(JSON.stringify({'message': message}));
        // clear input
        input.value = '';
        input.focus();
    }
});

input.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        // cancel the default action, if needed
        event.preventDefault();
        // trigger click event on button
        submitButton.click();
    }
});

input.focus();
const groupPk = document.getElementById("groupPk").value;
const webSocket = new WebSocket(`ws://${window.location.host}/ws/group/${groupPk}/`);

webSocket.onmessage = event => {
    let data = JSON.parse(event.data);

    if (data.type === 'chat') {
        let messages = document.getElementById('messages-container-scroll');
        let dateTime = new Date(data.date_time);
        dateTime = dateTime.toLocaleString();

        messages.insertAdjacentHTML(
            'beforeend',
            `
            <img src='${data.avatar}'>
            <div class="message">
                <p>
                    <b>${data.username}: </b>${data.message} (${dateTime})
                </p>
                <i>Переглядів: ${data.views}</i>
            </div>`
        );
    }
};

let messageForm = document.querySelector('.chat-form');

messageForm.addEventListener('submit', event => {
    event.preventDefault();

    let data_message = event.target.message.value;

    webSocket.send(JSON.stringify({
        'message': data_message
    }));

    event.target.message.value = '';
});

let isoDateTimeArray = document.querySelectorAll(".iso-date-time");

isoDateTimeArray.forEach(dateElem => {
    let newDate = new Date(dateElem.textContent);
    let dateToLocal = newDate.toLocaleString();
    dateElem.textContent = dateToLocal;
});

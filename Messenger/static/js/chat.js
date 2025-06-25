const contacts = document.querySelectorAll('.contact');
const chat = document.querySelector('.chat-container');

function insert() {
    chat.innerHTML = `
        <div id="messages-container-scroll" class="column"></div>
        <form method="post" class="chat-form">
            <input type="text" name="message" placeholder="Повідомлення" autocomplete="off" required>
            <div>
                <button type="button" id="form-emoji-btn" class="center"><img src="../static/img/emoji.svg"></button>
                <input type="file" style="display: none;">
                <button type="button" id="form-img-btn" class="center"><img src="../static/img/img.svg"></button>
                <button type="submit" id="form-send-btn" class="center"><img src="../static/home_app/img/PlaneR.png"></button>
            </div>
        </form>
    `;
}


contacts.forEach(btn => {
    btn.addEventListener('click', () => {
        insert();
        contacts.forEach(c => c.classList.remove('active'));
        btn.classList.add('active');
        sessionStorage.setItem('chat', btn.dataset.id);
    });
});

const savedChatId = sessionStorage.getItem('chat');
if (savedChatId) {
    const savedBtn = document.querySelector(`.contact[data-id="${savedChatId}"]`);
    if (savedBtn) {
        insert();
        savedBtn.classList.add('active');
    }
}
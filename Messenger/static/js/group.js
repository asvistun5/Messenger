const btn = document.getElementById('create-new-group-btn');
const modal = document.querySelector('.window-back');
const counter = document.getElementById('selected-users-counter');
const checkboxes = document.querySelectorAll('.select-user-checkbox');

const next = document.getElementById('next-btn');
const close = document.getElementById('close-btn');
const cancel = document.getElementById('cancel-btn');
//const upload = document.getElementById('post-img');
//const uploadbtn = document.getElementById('post-img-btn');

const winContent = document.querySelector('.window-content');
const contactsContainer = document.querySelector('.select-contacts-container');
const allContacts = document.getElementById('all-contacts-list');
const contactNames = document.querySelectorAll('.select-contact-name');

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const grouped = {};
let selected = 0;
let selectedIds = [];


contactNames.forEach(contact => {
    const name = contact.textContent.trim();
    const letter = name.charAt(0).toUpperCase();

    if (!grouped[letter]) {
        grouped[letter] = [];
    }
    grouped[letter].push(contact.closest('.select-contact'));
});


btn.addEventListener('click', () => {
    modal.classList.toggle('show');
});

close.addEventListener('click', () => {
    modal.classList.remove('show');
});

cancel.addEventListener('click', () => {
    modal.classList.remove('show');
});

for (const letter of alphabet) {
    if (grouped[letter]) {
        const header = document.createElement('p');
        header.className = 'filter-letter';
        header.textContent = letter;
        contactsContainer.appendChild(header);

        grouped[letter].forEach(contact => {
            contactsContainer.appendChild(contact);
        });
    }
}

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('click', () => {
        const parentId = checkbox.parentElement.parentElement.id;

        if (checkbox.checked) {
            selected++;
            if (!selectedIds.includes(parentId)) {
                selectedIds.push(parentId.match(/\d+/g));
            }
        } else {
            selected = Math.max(0, selected - 1);
            const index = selectedIds.indexOf(parentId);
            if (index !== -1) {
                selectedIds.splice(index, 1);
            }
        }

        counter.textContent = `Вибрано: ${selected}`;
    })
});

next.addEventListener('click', function onNextClick() {
    if (selected <= 1) {
        counter.textContent = 'Виберіть принаймні не менш 2 користувачів!';
    } else {
        winContent.innerHTML = `
        <p>Назва</p>
        <input type="text" id="group-preview-name" placeholder="Введіть назву" name="group-name">
        <div id="group-preview-container">
            <div class="center">
                <div id="group-preview-photo-container">
                    <p>NG</p>
                </div>
            </div>
            <input id="group-preview-input" type="file" style="display: none;" name="group-photo">
            <div class="center" style="gap: 24px;">
                <button class="group-preview-upload-btn"><img src="/static/img/plus.svg">Додайте фото</button>
                <button class="group-preview-upload-btn"><img src="/static/home_app/img/picture.png">Оберіть фото</button>
            </div>
        </div>
        <p>Учасники</p>
        <div class="group-preview-users-container">
        ${selectedIds}
        </div>
        `;
        cancel.textContent = 'Назад';
        next.textContent = 'Створити групу';
        /*setInterval(() => {
            next.type = 'submit';
        }, 1000);*/

        function getCookie(name) {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
            return cookieValue;
        }

        const groupNameInp = document.getElementById('group-preview-name');
        const groupPhotoCon = document.getElementById('group-preview-photo-container');

        next.removeEventListener('click', onNextClick);
        next.style.cursor = 'pointer';
        next.addEventListener('click', () => {
            fetch('/messages/', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    name: groupNameInp.value,
                    users: selectedIds,
                }),
            })
            if (groupNameInp.value.trim() === '') {
                alert(`Ведіть і'мя групи тут`);
                return;
            }
            modal.classList.remove('show');
        })

        document.querySelectorAll('.group-preview-upload-btn').forEach(btn => {
            btn.addEventListener('click', event => {
                event.preventDefault();
                document.getElementById('group-preview-input').click();
            })
        });

        let photoChanged = false;

        groupNameInp.addEventListener('input', () => {
            if (photoChanged == false) {
                const initials = groupNameInp.value
                    .split(' ')
                    .slice(0, 2)
                    .map(name => name[0])
                    .join('');

                if (groupNameInp.value !== '') {
                    groupPhotoCon.textContent = initials;
                }
            }
        })

        document.getElementById('group-preview-input').addEventListener('change', (event) => {
            const file = event.target.files[0];
                
            if (file) {
                const reader = new FileReader();
            
                reader.onload = e => {
                    groupPhotoCon.innerHTML = `<img src="${e.target.result}">`;
                    photoChanged = true;
                };
            
                reader.readAsDataURL(file);
            }
        })
    }
})
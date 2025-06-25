/*const editInput = document.getElementById('user-photo-input');
const editDisplayBtn = document.getElementById('user-photo-edit-btn');
const userPhoto = document.querySelector('.user-profile-photo');

const personalContainer = document.querySelector('.info-group');
const personalInputs = personalContainer.querySelectorAll('input');
const editPersonalBtn = document.getElementById('personal-info-edit-btn');

const editAutographBtn = document.getElementById('autograph-edit-btn');
const autographInput = document.getElementById('autograph-input');
const autographImg = document.getElementById('user-autograph');

let displayInfoEdit = false;
let personalInfoEdit = false;
let autographEdit = false;

function disableAllInputs() {
    personalInputs.forEach(input => input.disabled = true);
    autographInput.disabled = true;
}

editDisplayBtn.addEventListener('click', () => {
    displayInfoEdit = !displayInfoEdit;
    if (displayInfoEdit) {
        personalInfoEdit = false;
        autographEdit = false;
        disableAllInputs();
        editInput.click();
    } else {
        disableAllInputs();
    }
});

userPhoto.addEventListener('click', () => {
    if (displayInfoEdit) {
        editInput.click();
    }
});

editPersonalBtn.addEventListener('click', () => {
    if (!personalInfoEdit) {
        personalInfoEdit = true;
        displayInfoEdit = false;
        autographEdit = false;
        disableAllInputs();
        personalInputs.forEach(input => input.disabled = false);
    } else {
        personalInfoEdit = false;
        disableAllInputs();
    }
});

editAutographBtn.addEventListener('click', () => {
    if (!autographEdit) {
        autographEdit = true;
        personalInfoEdit = false;
        displayInfoEdit = false;
        disableAllInputs();
        autographInput.disabled = false;
        autographInput.click();
    } else {
        autographEdit = false;
        disableAllInputs();
    }
});

editInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            userPhoto.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});

autographInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            autographImg.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});

disableAllInputs();*/


const editInput = document.getElementById('user-photo-input');
const editDisplayBtn = document.getElementById('user-photo-edit-btn');
const userPhoto = document.querySelector('.user-profile-photo');

const personalContainer = document.querySelector('.info-group');
const personalInputs = personalContainer.querySelectorAll('input');
const editPersonalBtn = document.getElementById('personal-info-edit-btn');

const editAutographBtn = document.getElementById('autograph-edit-btn');
const autographInput = document.getElementById('autograph-input');
const autographImg = document.getElementById('user-autograph');

let displayInfoEdit = false;
let personalInfoEdit = false;
let autographEdit = false;

function disableAllInputs() {
    personalInputs.forEach(input => input.disabled = true);
    autographInput.disabled = true;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

editDisplayBtn.addEventListener('click', () => {
    displayInfoEdit = !displayInfoEdit;
    if (displayInfoEdit) {
        personalInfoEdit = false;
        autographEdit = false;
        disableAllInputs();
        editInput.click();
    } else {
        disableAllInputs();
    }
});

userPhoto.addEventListener('click', () => {
    if (displayInfoEdit) {
        editInput.click();
    }
});

editPersonalBtn.addEventListener('click', () => {
    if (!personalInfoEdit) {
        personalInfoEdit = true;
        displayInfoEdit = false;
        autographEdit = false;
        disableAllInputs();
        personalInputs.forEach(input => input.disabled = false);
    } else {
        personalInfoEdit = false;
        disableAllInputs();
    }
});

editAutographBtn.addEventListener('click', () => {
    if (!autographEdit) {
        autographEdit = true;
        personalInfoEdit = false;
        displayInfoEdit = false;
        disableAllInputs();
        autographInput.disabled = false;
        autographInput.click();
    } else {
        autographEdit = false;
        disableAllInputs();
    }
});

editInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('user_photo', file);

        fetch('/profile/upload-photo/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success && data.photo_url) {
                userPhoto.src = data.photo_url;
            } else {
                alert('Ошибка загрузки фото');
            }
        })
        .catch(() => alert('Ошибка сети'));
    }
});

autographInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('autograph', file);

        fetch('/profile/upload-autograph/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success && data.autograph_url) {
                autographImg.src = data.autograph_url;
            } else {
                alert('Ошибка загрузки автографа');
            }
        })
        .catch(() => alert('Ошибка сети'));
    }
});

personalInputs.forEach(input => {
    input.addEventListener('change', () => {
        const formData = new FormData();
        formData.append(input.name, input.value);

        fetch('/profile/update-info/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                alert('Ошибка обновления данных');
            }
        })
        .catch(() => alert('Ошибка сети'));
    });
});

disableAllInputs();
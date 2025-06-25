const btn = document.querySelector('.fast-message-content-button-publish');
const modal = document.querySelector('.window-back');

const close = document.getElementById('close-btn');
const upload = document.getElementById('post-img');
const uploadbtn = document.getElementById('post-img-btn');

let savedText = "";


btn.addEventListener('click', () => {
    modal.classList.toggle('show');
});

close.addEventListener('click', () => {
    modal.classList.remove('show');
});

uploadbtn.addEventListener('click', () => {
    upload.click();
});

setInterval(function() {
    savedText = $('.fast-message-content-input').val();
}, 1000);


$('.fast-message-content-button-publish').on('click', function() {
    $('#post-description').text(savedText);
});

const preview = document.querySelector('.img-preview-container');
const prevImg = document.getElementById('post-img');

let loadedImages = 0;

prevImg.addEventListener('change', event => {
    const file = event.target.files[0];

    if (!file) return;

    if (document.querySelectorAll('.img-preview-container').length >= 5) {
        alert('Максимум 3 зображення!');
        prevImg.value = '';
        return;
    }

    const reader = new FileReader();

    reader.onload = e => {
        loadedImages++;

        const clone = preview.cloneNode(true);
        const clonedImg = clone.querySelector('img');
        const delBtn = clone.querySelector('.img-delete-btn');

        clone.style.display = 'flex';
        clonedImg.src = e.target.result;
        clonedImg.style.display = 'block';
        delBtn.style.display = 'block';

        delBtn.addEventListener('click', () => {
            clone.remove();
        });

        preview.parentElement.insertBefore(clone, prevImg);
    };

    reader.readAsDataURL(file);
});
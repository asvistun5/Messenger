const pub = document.getElementById('publish-btn');

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

pub.addEventListener('click', event => {
    event.preventDefault();

    fetch('/create/', {
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

    window.location.href = 'http://127.0.0.1:8000/';
})
const area = document.getElementById('post-description');
const tags = document.querySelectorAll('.tag');

const addtag = document.getElementById('add-new-tag-btn');
const addlink = document.getElementById('add-new-link-btn');
const linkinput = document.querySelector('.social-link-field');


function addTagToArea(val) {
    const parts = area.value.split('\n\n');
    const userText = parts[0].trim();
    const existingTags = parts[1] ? parts[1].trim().split(' ') : [];

    if (!existingTags.includes(val)) {
        existingTags.push(val);
    }

    area.value = `${userText}\n\n${existingTags.join(' ')}`;
}

tags.forEach(tag => {
    const val = tag.textContent;

    tag.addEventListener('click', () => {
        addTagToArea(val);
    });
});

addtag.addEventListener('click', () => {
    const parent = addtag.parentElement;

    if (!document.getElementById('add-tag-input')) {
        const input = document.createElement('input');
        input.type = "text";
        input.id = "add-tag-input";
        input.placeholder = "Введіть тег";
        input.style.height = "30px";

        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const val = input.value.trim();
                if (!val) return;

                input.remove();

                const newTag = document.createElement('div');
                newTag.className = 'tag';
                newTag.textContent = `#${val}`;

                newTag.addEventListener('click', () => {
                    addTagToArea(`#${val}`);
                });

                parent.insertBefore(newTag, addtag);
                input.value = '';
            }
        });

        parent.insertBefore(input, addtag);
    }
});

addlink.addEventListener('click', () => {
    const parent = addlink.parentElement;
    const input = linkinput.cloneNode(true);

    parent.insertBefore(input, addlink);
})
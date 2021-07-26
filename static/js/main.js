function handleReply(response_id) {
    const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`)
    if (reply_form_container) {
        reply_form_container.style.display = 'block';
    }
}

function handleCancel(response_id) {
    const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`)
    if (reply_form_container) {
        reply_form_container.style.display = 'none';
    }
}

function searchBarShow() {
    const search_bar = document.querySelector(`#s-field`)
    if (search_bar) {
        if (search_bar.style.display == 'inline-block'){
            search_bar.style.display = 'none';
        }
        else {
            search_bar.style.display = 'inline-block';
            search_bar.focus();
        }
    }
}

function showMenu(btn) {
    const nav_bar = document.querySelector(`.navbar-nav`)
    if (nav_bar) {
        btn.classList.toggle('change');
        if (nav_bar.style.display == 'inline-block'){
            nav_bar.style.display = 'none';

        }
        else {
            nav_bar.style.display = 'inline-block';
            nav_btn.src = "icon_search.svg";
        }
    }
}
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')  // Replace & with -and-
        .replace(/[\s\W-]+/g, '-')  // Replace spaces, nonword chars, and dashes with a single dash. 
        .replace(/-$/, '').replace(/^-/, '') // Replace trailing and leading dashes
};

titleInput.addEventListener('keyup',(e) => {
    slugInput.setAttribute('value', slugify(titleInput.value))
});
console.log('hello world');

const copyBtns = [...document.getElementsByClassName('copy-btn')];
console.log(copyBtns);

let previous = null;

copyBtns.forEach(btn => btn.addEventListener('click', ()=> {
    console.log('clicked');
    const photoUrl = btn.getAttribute('data-url');
    console.log(photoUrl);
    navigator.clipboard.writeText(photoUrl);
    btn.textContent='Copied!';

    if (previous) {
        btn.textContent='Copy image url'
    }
    previous = btn
}))
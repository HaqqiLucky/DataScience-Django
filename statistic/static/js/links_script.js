document.querySelectorAll('.link-to-detail').forEach(button => {
    button.addEventListener('click', function(){
        console.log(this)
        window.location.href = this.getAttribute('data-url');
    });
});
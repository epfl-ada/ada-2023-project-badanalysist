document.querySelectorAll('.topic .box').forEach(function(topicBox, index) {
    topicBox.addEventListener('click', function() {
        var blurb = document.querySelector('#blurb' + (index + 1));
        var selectedBox = document.querySelector('.box.selected');

        if (blurb) {
            requestAnimationFrame(function() {
                blurb.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            });
        }

        topicBox.classList.add('selected');

        if (selectedBox && selectedBox !== topicBox) {
            selectedBox.classList.remove('selected');
        }
    });
});

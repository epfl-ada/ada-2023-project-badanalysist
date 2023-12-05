document.querySelector('.content').addEventListener('wheel', function(e) {
    e.preventDefault();
    var scrollPosition = document.querySelector('.content').scrollLeft;
    var sections = document.querySelectorAll('.content-section');
    var boxes = document.querySelectorAll('.topic .box');
    this.scrollLeft += e.deltaY;

    boxes.forEach(function(box) {
        box.classList.remove('selected');
    });

    sections.forEach(function(section, index) {
        var sectionStart = section.offsetLeft;
        var sectionEnd = sectionStart + section.offsetWidth;

        if (scrollPosition >= sectionStart && scrollPosition < sectionEnd) {
            boxes[index].classList.add('selected');
        }
    });
});

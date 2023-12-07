window.addEventListener('wheel', function() {
    var topic = document.querySelector('.topic');
    var topicOffset = topic.getBoundingClientRect().top;

    var scrollPrompt = document.querySelector('.scroll-prompt');
    var scrollPromptTop = scrollPrompt.getBoundingClientRect().top;
    var viewportHeight = window.innerHeight;
    var scrollPromptTopVh = (scrollPromptTop / viewportHeight) * 100;

    if (topicOffset <= 0 && scrollPromptTopVh <= -12) {
        topic.style.position = 'fixed';
        topic.style.top = '0';
        topic.style.backgroundColor = 'rgba(250, 249, 238, 0.7)';
    } else {
        topic.style.position = 'absolute';
        topic.style.top = '102vh';
        topic.style.backgroundColor = 'transparent'; 
    }

    var sections = document.querySelectorAll('.content-section');
    var topics = document.querySelectorAll('.topic .box');

    sections.forEach(function(section, index) {
        var sectionRect = section.getBoundingClientRect();
        var topic = topics[index];

        if (sectionRect.top <= window.innerHeight * 0.6) {
            topic.classList.add('selected');
            
            if (index >= 1 && topics[index - 1]) {
                topics[index - 1].classList.remove('selected');
            }
        }

        if (sectionRect.top > window.innerHeight * 0.6) {
            topic.classList.remove('selected');
        }
    });
});

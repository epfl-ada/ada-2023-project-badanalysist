window.addEventListener('wheel', function() {
    var topic = document.querySelector('.topic');
    var topicOffset = topic.getBoundingClientRect().top; 

    if (topicOffset <= 0) {
        topic.style.position = 'fixed';
        topic.style.top = '0'; 
    } else {
        topic.style.position = 'absolute'; 
        topic.style.top = null; 
    }
});

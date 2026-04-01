barba.init({
    transitions: [
        {
            name: 'fade',
            leave(data) {
                return new Promise(function (resolve) {
                    data.current.container.style.transition = 'opacity 0.2s ease-out';
                    data.current.container.style.opacity = 0;
                    setTimeout(resolve, 200);
                });
            },
            enter(data) {
                data.next.container.style.opacity = 0;
                return new Promise(function (resolve) {
                    requestAnimationFrame(function () {
                        data.next.container.style.transition = 'opacity 0.2s ease-in';
                        data.next.container.style.opacity = 1;
                        setTimeout(resolve, 200);
                    });
                });
            },
            after() {
                window.scrollTo(0, 0);
            }
        }
    ],
    prevent: function (ref) {
        var el = ref.el;
        return el.hasAttribute('target') && el.getAttribute('target') === '_blank';
    }
});

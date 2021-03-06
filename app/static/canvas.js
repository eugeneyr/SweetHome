var registeredRenderers = Array();

function render() {
    for (func in registeredRenderers) {
        func();
    }
}

window.requestAnimFrame = (function () {
    return window.requestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        window.oRequestAnimationFrame ||
        window.msRequestAnimationFrame || function (callback) {
        window.setTimeout(callback, 1000 / 60);
    };
})();

(function animloop() {
    requestAnimFrame(animloop);
    render();
})();

function registerRenderer(renderFunc) {
    registeredRenderers.push(renderFunc);
}
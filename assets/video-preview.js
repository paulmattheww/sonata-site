(() => {
    const video = document.querySelector('.preview-player');
    if (!video || !('IntersectionObserver' in window)) return;

    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let visible = false;
    let playbackRequested = false;

    function updatePlayback() {
        if (!visible || document.hidden) {
            video.pause();
            return;
        }
        if (playbackRequested || reducedMotion.matches || navigator.connection?.saveData) return;
        playbackRequested = true;
        if (!video.paused || video.ended) return;
        video.muted = true;
        const playback = video.play();
        if (playback) playback.catch(() => {});
    }

    video.addEventListener('play', () => {
        playbackRequested = true;
    });
    const visibility = new IntersectionObserver(entries => {
        visible = entries[0].isIntersecting && entries[0].intersectionRatio >= 0.5;
        updatePlayback();
    }, { threshold: [0, 0.5] });
    visibility.observe(video);
    document.addEventListener('visibilitychange', updatePlayback);
    reducedMotion.addEventListener('change', () => {
        if (reducedMotion.matches) video.pause();
        else updatePlayback();
    });
})();

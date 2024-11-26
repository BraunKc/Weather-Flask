const autoDetectBtn = document.getElementById('auto-detect-btn');

autoDetectBtn.addEventListener('click', () => {
  navigator.geolocation.getCurrentPosition(position => {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    fetch('/get_cords', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({lat: lat, lon:lon}),
    })
    .then(response => response.json())
    .then(data => {
      window.location.href = `/${data.city}`
    })
  });
});
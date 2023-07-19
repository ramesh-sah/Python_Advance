window.addEventListener('DOMContentLoaded', (event) => {
    const divs = document.querySelectorAll('div');
    divs.forEach((div, index) => {
        div.classList.add('highlight');
        div.innerHTML = index + 1 + div.innerHTML;
    });

    const numbers = {{ numbers|safe }};
    if (numbers.length > 0) {
        numbers.forEach((number) => {
            if (number > 20) {
                const div = document.createElement('div');
                div.textContent = number;
                document.getElementById('dynamic-content').appendChild(div);
            }
        });
    } else {
        const div = document.createElement('div');
        div.textContent = 'No data found';
        div.classList.add('hidden');
        document.getElementById('dynamic-content').appendChild(div);
    }
});

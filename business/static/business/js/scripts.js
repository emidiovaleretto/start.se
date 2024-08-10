function updateRangeValue(rangeInput) {
    const value = rangeInput.value;
    const rangeValue = document.getElementById('rangeValue');
    rangeValue.textContent = value + '%';

    const rangeWidth = rangeInput.offsetWidth;
    const thumbWidth = 16;
    const offset = (value / rangeInput.max) * (rangeWidth - thumbWidth);
    
    rangeValue.style.left = `calc(${offset}px + ${thumbWidth / 2}px)`;
}

document.addEventListener('DOMContentLoaded', function() {
    const rangeInput = document.getElementById('business_percentage_return');
    updateRangeValue(rangeInput);
});
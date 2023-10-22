document.addEventListener('DOMContentLoaded', function() {
    const selectionSpan = document.getElementById('selection');
    const bitcoinCountSpan = document.getElementById('bitcoinCount');
    const goldCountSpan = document.getElementById('goldCount');
    const silverCountSpan = document.getElementById('silverCount');
    const currencyButtons = document.querySelectorAll('.currency-button');

    // Initialize counts from localStorage or set to 0 if not present
    let bitcoinCount = parseInt(localStorage.getItem('bitcoinCount')) || 0;
    let goldCount = parseInt(localStorage.getItem('goldCount')) || 0;
    let silverCount = parseInt(localStorage.getItem('silverCount')) || 0;

    //  // Initialize counts and set to 0 
    //  let bitcoinCount = 0;
    //  let goldCount = 0;
    //  let silverCount = 0;

    bitcoinCountSpan.textContent = bitcoinCount;
    goldCountSpan.textContent = goldCount;
    silverCountSpan.textContent = silverCount;

    currencyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const selectedCurrency = button.getAttribute('data-currency');
            selectionSpan.textContent = selectedCurrency;
            
            // Update the count based on the selected currency
            switch (selectedCurrency) {
                case 'Bitcoin':
                    bitcoinCount++;
                    localStorage.setItem('bitcoinCount', bitcoinCount);
                    bitcoinCountSpan.textContent = bitcoinCount;
                    break;
                case 'Gold':
                    goldCount++;
                    localStorage.setItem('goldCount', goldCount);
                    goldCountSpan.textContent = goldCount;
                    break;
                case 'Silver':
                    silverCount++;
                    localStorage.setItem('silverCount', silverCount);
                    silverCountSpan.textContent = silverCount;
                    break;
                default:
                    break;
            }
        });
    });
});

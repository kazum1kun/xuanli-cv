// Close the mobile menu before following a homepage section link.
const menu = document.querySelector('#nav-menu');
const toggle = document.querySelector('#nav-toggle');
menu?.addEventListener('click', (event) => {
  if (event.target.closest('a') && toggle?.checked) {
    toggle.checked = false;
    toggle.dispatchEvent(new Event('change', { bubbles: true }));
  }
});

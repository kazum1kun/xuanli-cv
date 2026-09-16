// The full archive remains readable if JavaScript is unavailable.
const archive = document.querySelector('.xlin-publications');

if (archive) {
  const form = archive.querySelector('[data-publication-filters]');
  const search = form.elements.namedItem('q');
  const year = form.elements.namedItem('year');
  const type = form.elements.namedItem('type');
  const count = archive.querySelector('[data-publication-count]');
  const empty = archive.querySelector('[data-publication-empty]');
  const normalize = (text) => text.normalize('NFKD').replace(/\p{M}/gu, '').toLocaleLowerCase();
  const publications = Array.from(archive.querySelectorAll('[data-publication]'), (element) => ({
    element,
    search: normalize(element.dataset.search),
    year: element.dataset.year,
    types: element.dataset.types.split(' '),
  }));

  function filterPublications() {
    const terms = normalize(search.value).trim().split(/\s+/u).filter(Boolean);
    let visible = 0;

    for (const publication of publications) {
      const matches = (!year.value || publication.year === year.value)
        && (!type.value || publication.types.includes(type.value))
        && terms.every((term) => publication.search.includes(term));
      publication.element.hidden = !matches;
      if (matches) visible += 1;
    }

    const filtered = terms.length > 0 || year.value !== '' || type.value !== '';
    count.textContent = filtered
      ? `${visible} of ${publications.length} publications`
      : `${visible} ${visible === 1 ? 'publication' : 'publications'}`;
    empty.hidden = visible !== 0;
  }

  form.addEventListener('input', filterPublications);
  form.addEventListener('change', filterPublications);
  form.addEventListener('submit', (event) => event.preventDefault());
  form.addEventListener('reset', () => {
    // Reset events precede the browser's restoration of the form controls.
    window.setTimeout(() => {
      filterPublications();
      search.focus();
    }, 0);
  });
  filterPublications();
  form.hidden = false;
}

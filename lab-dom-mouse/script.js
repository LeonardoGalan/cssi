
button.addEventListener('mouseover', () => {
  button.innerHTML = 'Don/'t click!';
  button.classList.add('danger');
});

button.addEventListener('mouseout', () => {
  button.innerHTML = 'Click me!';
  button.classList.remove('danger');
});

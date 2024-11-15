const categoryLinks = document.querySelectorAll('.category-link');
const categories = document.querySelectorAll('.category');

categoryLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();

    // Hide
    categories.forEach(category => {
      category.style.display = 'none';
    });

    // Show
    const categoryId = e.target.getAttribute('data-category');
    const selectedCategory = document.getElementById(categoryId);
    selectedCategory.style.display = 'block';
  });
});


// By default, entrepreneurs category is shown
document.addEventListener("DOMContentLoaded", () => {
  const defaultCategory = document.getElementById("business-leaders");

  if (defaultCategory) {
      defaultCategory.style.display = "block";
  }
});

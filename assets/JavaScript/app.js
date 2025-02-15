document.addEventListener("DOMContentLoaded", function () {
  // Add animation order to projects
  const projects = document.querySelectorAll(".project");
  projects.forEach((project, index) => {
    project.style.setProperty("--order", index);
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });
});

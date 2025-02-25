document.addEventListener("DOMContentLoaded", function () {
  // Add hover effect to logo container
  const logoWrapper = document.querySelector(".logo-wrapper");
  const logo = document.querySelector(".rotating-logo");

  if (logoWrapper && logo) {
    logoWrapper.addEventListener("mouseenter", () => {
      logo.style.animationDuration = "10s"; // Speed up rotation on hover
    });

    logoWrapper.addEventListener("mouseleave", () => {
      logo.style.animationDuration = "20s"; // Return to normal speed
    });
  }

  // Add smooth scroll effect to banner icons
  const bannerIcons = document.querySelectorAll(".banner-icon");
  bannerIcons.forEach((icon) => {
    icon.addEventListener("mouseenter", () => {
      // Add a slight pause to the banner animation on hover
      const bannerContent = document.querySelector(".banner-content");
      if (bannerContent) {
        bannerContent.style.animationPlayState = "paused";
      }
    });

    icon.addEventListener("mouseleave", () => {
      // Resume banner animation
      const bannerContent = document.querySelector(".banner-content");
      if (bannerContent) {
        bannerContent.style.animationPlayState = "running";
      }
    });
  });
});

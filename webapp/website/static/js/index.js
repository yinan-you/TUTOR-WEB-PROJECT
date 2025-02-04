gsap.registerPlugin(ScrollTrigger);

gsap.to(".scroll-circle", {
  scrollTrigger: {
    trigger: ".scroll-circle", // Element that triggers the animation
    start: "top 80%", // When the top of the trigger hits 80% of the viewport height
    end: "top 40%", // Ends the animation when the top of the trigger hits 20%
    scrub: true, // Makes the animation smooth and linked to the scroll
  },
  y: "40vh", // Moves the circle 200px along the Y-axis
  x: "40vh",
  ease: "power1.inOut",
});

const text = document.getElementById("drawText"); // Make sure this matches the ID in your HTML

if (text) {
  const length = text.getTotalLength(); // Get the total length of the stroke

  // Set initial stroke state
  text.style.strokeDasharray = length;
  text.style.strokeDashoffset = length;

  // Animate stroke dashoffset on scroll
  gsap.to(text, {
    scrollTrigger: {
      trigger: "#drawText", // Element to trigger the animation
      start: "top 75%", // Trigger when top of element is 75% from the top of viewport
      end: "bottom top", // End the animation when the bottom of the element reaches the top of the viewport
      scrub: true, // Make the animation scrubbable with scroll
      markers: true, // Show markers for debugging (remove this when not needed)
    },
    strokeDashoffset: 0, // Animate stroke to 0 (fully drawn)
    duration: 2, // Duration of the animation
    ease: "power1.inOut", // Ease for smooth animation
  });
} else {
  console.error("Text element not found");
}

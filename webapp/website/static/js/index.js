gsap.registerPlugin(ScrollTrigger);

gsap.from(".box", {
  opacity: 0,
  y: 100,
  duration: 1,
  scrollTrigger: {
    trigger: ".box",
    start: "top 80%", // Starts animation when top of .box reaches 80% of viewport
    end: "top 30%", // Ends at 30% of viewport
    scrub: true, // Smooth animation while scrolling
  },
});

gsap.to(".background", {
  yPercent: 50, // Moves the background down 50% as you scroll
  ease: "none",
  scrollTrigger: {
    trigger: ".parallax-wrapper",
    start: "top top", // Start when the top of the parallax container reaches the top of the viewport
    end: "bottom top", // End when the bottom of the parallax container reaches the top of the viewport
    scrub: true, // Smooth scroll effect
  },
});

gsap.to(".scroll-circle", {
  scrollTrigger: {
    trigger: ".scroll-circle", // Element that triggers the animation
    start: "top 80%", // When the top of the trigger hits 80% of the viewport height
    end: "top 40%", // Ends the animation when the top of the trigger hits 20%
    scrub: true, // Makes the animation smooth and linked to the scroll
    markers: true, // Optional, shows markers for debugging
  },
  y: "40vh", // Moves the circle 200px along the Y-axis
  x: "40vh",
  ease: "power1.inOut",
});

gsap.from("#drawText", {
  duration: 2, // Duration of animation (2 seconds)
  strokeDasharray: 1000, // Total length of the stroke path (we will animate along this path)
  strokeDashoffset: 1000, // Start the dash off completely hidden
  ease: "power1.inOut", // Easing for smooth animation
  markers: true,
});

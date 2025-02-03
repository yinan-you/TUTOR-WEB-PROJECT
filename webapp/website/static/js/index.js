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

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

const letters = document.querySelectorAll(".letter");

letters.forEach((letter) => {
  const length = letter.getTotalLength();
  letter.style.strokeDasharray = length;
  letter.style.strokeDashoffset = length;

  gsap.to(letter, {
    strokeDashoffset: 0,
    ease: "power1.inOut",
    scrollTrigger: {
      trigger: letter,
      start: "top 70%", // Start drawing earlier
      end: "top 20%", // Finish faster
      scrub: 0.5, // Faster scrub (lower = quicker)
      markers: false,
    },
  });
});

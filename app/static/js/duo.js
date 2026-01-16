document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll(".tilt-3d");
  const maxTilt = 15;

  elements.forEach((el) => {
    el.style.transformStyle = "preserve-3d";
    el.style.display = "inline-block";

    el.addEventListener("mousemove", (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -maxTilt;
      const rotateY = ((x - centerX) / centerX) * maxTilt;

      el.style.transform = `
        perspective(600px)
        rotateX(${rotateX}deg)
        rotateY(${rotateY}deg)
        scale(1.05)
      `;
    });

    el.addEventListener("mouseleave", () => {
      el.style.transform = `
        perspective(600px)
        rotateX(0deg)
        rotateY(0deg)
        scale(1)
      `;
    });
  });
});

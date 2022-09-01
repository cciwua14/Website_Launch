const modalBtn = document.querySelector(".modal-btn");
const modalBg = document.querySelector(".modal-bg");
const modalClose = document.querySelector(".modal-close");

if (modalBtn) {
    modalBtn.addEventListener("click", () => {
      modalBg.classList.add("bg-active");
    });
  }
  
  if (modalClose) {
    modalClose.addEventListener("click", () => {
      modalBg.classList.remove("bg-active");
    });
  }
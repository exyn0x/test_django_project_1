// Landing page scripts: mobile menu, footer year, double-submit guard.

(function () {
  "use strict";

  // 1. Mobile menu: open and close the dropdown
  var menuButton = document.querySelector(".menu-btn");
  var navLinks = document.querySelector(".nav-links");

  function setMenu(open) {
    navLinks.classList.toggle("is-open", open);
    menuButton.setAttribute("aria-expanded", String(open));
  }

  if (menuButton && navLinks) {
    menuButton.addEventListener("click", function () {
      setMenu(!navLinks.classList.contains("is-open"));
    });

    // Close the menu after a click on any link inside it
    navLinks.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        setMenu(false);
      }
    });

    // Close the menu with the Escape key
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        setMenu(false);
      }
    });
  }

  // 2. Footer year, so you never update it by hand
  var yearEl = document.querySelector("[data-year]");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // 3. Disable the submit button after the first click (no double submits)
  var form = document.querySelector(".contact-form");
  var submitBtn = form ? form.querySelector('button[type="submit"]') : null;

  if (form && submitBtn) {
    var defaultLabel = submitBtn.textContent;

    form.addEventListener("submit", function () {
      submitBtn.disabled = true;
      submitBtn.textContent = "Sending…";
    });

    // The browser "Back" button can restore the page with the button still
    // disabled, so reset it whenever the page is shown again.
    window.addEventListener("pageshow", function () {
      submitBtn.disabled = false;
      submitBtn.textContent = defaultLabel;
    });
  }
})();

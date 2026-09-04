/* ============================================================
   LUXE BEAUTY YANCHEP — site behaviour

   >>> CHANGE THE BOOKING LINK IN ONE PLACE: BOOKING_URL below. <<<
   Every "Book now" button on every page reads from it.
   Paste the Fresha / Square / Timely / Bookla link there and the
   whole site updates. Until then it falls back to Instagram DMs.
   ============================================================ */

const BOOKING_URL = "https://squareup.com/appointments/book/Q0QM7TJZ6949G";

const CONTACT = {
  instagram: "https://www.instagram.com/luxebeautyyanchep/",
  email:     "",          // waiting on a Luxe-branded address; the old
                          // blushbeautyparlour@outlook.com is off-brand now
  phone:     "0411 487 177"
};

document.addEventListener("DOMContentLoaded", function () {

  /* --- booking links --------------------------------------- */
  document.querySelectorAll("[data-book]").forEach(function (a) {
    a.href = BOOKING_URL;
    if (/^https?:/i.test(BOOKING_URL)) { a.target = "_blank"; a.rel = "noopener"; }
  });

  /* --- contact links: hide any that aren't filled in yet ---- */
  document.querySelectorAll("[data-contact]").forEach(function (el) {
    var k = el.getAttribute("data-contact"), v = CONTACT[k];
    if (!v) { el.hidden = true; return; }
    if (k === "email") { el.href = "mailto:" + v; el.textContent = v; }
    if (k === "phone") { el.href = "tel:" + v.replace(/\s+/g, ""); el.textContent = v; }
    if (k === "instagram") { el.href = v; }
  });

  /* --- mobile nav ------------------------------------------ */
  var tog = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (tog && nav) {
    tog.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      tog.setAttribute("aria-expanded", open ? "true" : "false");
      tog.textContent = open ? "✕" : "☰";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        tog.setAttribute("aria-expanded", "false");
        tog.textContent = "☰";
      }
    });
  }

  /* --- gallery: swap in a real photo if the file exists ----
     Placeholders stay until photos are dropped into /photos.  */
  document.querySelectorAll(".shot[data-photo]").forEach(function (fig) {
    var src = fig.getAttribute("data-photo");
    var probe = new Image();
    probe.onload = function () {
      var img = document.createElement("img");
      img.src = src;
      img.alt = fig.getAttribute("data-alt") || "Luxe Beauty Yanchep lash and brow work";
      img.loading = "lazy";
      var ph = fig.querySelector(".ph");
      if (ph) ph.remove();
      fig.prepend(img);
    };
    probe.src = src;
  });

  /* --- reveal on scroll ------------------------------------ */
  if (!matchMedia("(prefers-reduced-motion:reduce)").matches && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".rv").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".rv").forEach(function (el) { el.classList.add("in"); });
  }

  /* --- footer year ----------------------------------------- */
  var y = document.getElementById("yr");
  if (y) y.textContent = new Date().getFullYear();
});

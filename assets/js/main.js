// active nav link
(function(){
  const path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".links a").forEach(a => {
    const href = a.getAttribute("href");
    if ((path === "index.html" && href === "index.html") || href === path) {
      a.setAttribute("aria-current", "page");
    }
  });

  // footer year
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
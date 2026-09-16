const input = document.querySelector("#log-search");
const rows = Array.from(document.querySelectorAll("#log-body tr"));
const count = document.querySelector("#visible-count");
const empty = document.querySelector("#empty-state");

if (input && rows.length) {
  input.addEventListener("input", () => {
    const q = input.value.trim().toLocaleLowerCase("zh-CN");
    let n = 0;
    rows.forEach((row) => {
      const hay = `${row.textContent} ${row.dataset.search || ""}`.toLocaleLowerCase("zh-CN");
      const hit = !q || hay.includes(q);
      row.hidden = !hit;
      if (hit) n += 1;
    });
    if (count) count.textContent = String(n);
    if (empty) empty.hidden = n !== 0;
  });
}

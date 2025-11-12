function attachSearch(
  btnId = "searchBtn",
  selectId = "searchCategory",
  inputSelector = ".search-input"
) {
  const btn = document.getElementById(btnId);
  const select = document.getElementById(selectId);
  const input = document.querySelector(inputSelector);
  if (!btn || !select) return;
  btn.addEventListener("click", function () {
    const base = select.value || "/";
    const q = input && input.value.trim() ? input.value.trim() : "";
    let url = base;
    if (q) {
      url +=
        (base.indexOf("?") === -1 ? "?" : "&") + "q=" + encodeURIComponent(q);
    }
    window.location.href = url;
  });
}



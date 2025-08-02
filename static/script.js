// ========== SHOW/HIDE PASSWORD ==========
const pwInput = document.getElementById("password");
const pwEye = document.getElementById("pw-eye");
let isVisible = false;

pwEye.addEventListener("click", togglePasswordEye);
pwEye.addEventListener("keydown", (e) => {
  if (e.key === "Enter" || e.key === " ") togglePasswordEye();
});

function togglePasswordEye() {
  isVisible = !isVisible;
  pwInput.type = isVisible ? "password" : "text";
  pwEye.src = isVisible
    ? "/static/assets/2767146.png"
    : "/static/assets/709612.png";
}

// ========== PASSWORD STRENGTH BAR ==========
const pwStrengthBar = document.getElementById("pw-strength-bar");
const pwResult = document.getElementById("pw-result");

function getStrengthLevel(pw) {
  if (!pw) return 0;
  if (pw.length < 6) return 1; // Very weak
  if (pw.length < 8) return 2; // Weak

  let hasLower = /[a-z]/.test(pw);
  let hasUpper = /[A-Z]/.test(pw);
  let hasNumber = /[0-9]/.test(pw);
  let hasSpecial = /[^A-Za-z0-9]/.test(pw);
  let types = [hasLower, hasUpper, hasNumber, hasSpecial].filter(Boolean).length;

  if (types === 1) return 2; // Weak
  if (types === 2) return 3; // Fair
  if (types >= 3) return 4; // Strong
  return 1;
}

// ========== PROGRESS INPUT DEBOUNCE + FETCH ==========
let debounceTimer;
pwInput.addEventListener("input", function () {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    const val = pwInput.value.trim();
    let level = val ? getStrengthLevel(val) : 0;

    pwStrengthBar.className = "pw-strength-bar";
    if (level > 0) {
      pwStrengthBar.classList.add("level-" + level);
    }

    if (!val) {
      pwResult.innerHTML = "";
      return;
    }

    // Fetch API check password from backend
    fetch("/check", {
      method: "POST",
      body: new URLSearchParams({ password: val }),
    })
      .then((res) => res.json())
      .then((data) => {
        renderResult(data);
      })
      .catch(() => {
        pwResult.innerHTML =
          `<div class="pw-warning">Connection error to server/backend!</div>`;
      });
  }, 600); // Wait 600ms after stop to send request
});

// ========== RESULT ==========
function renderResult(data) {
  if (data.ok === false) {
    pwResult.innerHTML =
      `<div class="pw-warning">${data.msg || "Error!"}</div>`;
    pwStrengthBar.className = "pw-strength-bar"; // Reset bar if error
    return;
  }
  pwStrengthBar.className = "pw-strength-bar";
  if (data.strength_level > 0) {
    pwStrengthBar.classList.add("level-" + data.strength_level);
  }
  pwResult.innerHTML = `
    <div class="pw-strength-text level-${data.strength_level}">
      ${data.strength}
    </div>
    <div>${
      data.suggestions && data.suggestions.length
        ? data.suggestions.join("<br>")
        : ""
    }</div>
    <div>Entropy: ${data.entropy || "N/A"}</div>
    <div>${
      data.pwned
        ? `<span style="color: red;">Password has been leaked (${data.pwned} times)</span>`
        : ""
    }</div>
  `;
}

// Prevent form submit from reloading the page on Enter
const pwForm = document.getElementById("pw-form");
if (pwForm) {
  pwForm.addEventListener("submit", function(e) {
    e.preventDefault();
    // Xử lý password ở đây thôi, KHÔNG reload trang!
    return false;
  });
}

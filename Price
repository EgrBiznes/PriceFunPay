<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Price Calculator</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>

  <style>
    body {
      margin: 0;
      padding: 16px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial;
      background: #ffffff;
    }

    h1 {
      font-size: 18px;
      margin-bottom: 12px;
    }

    input {
      width: 100%;
      box-sizing: border-box;
      padding: 14px;
      font-size: 18px;
      border-radius: 10px;
      border: 1px solid #ddd;
      margin-bottom: 12px;
    }

    button {
      width: 100%;
      padding: 14px;
      font-size: 18px;
      background: #2aabee;
      color: white;
      border: none;
      border-radius: 10px;
      cursor: pointer;
    }

    button:active {
      opacity: 0.85;
    }

    img {
      margin-top: 16px;
      width: 100%;
      border-radius: 14px;
      display: none;
    }
  </style>
</head>
<body>

<h1>Введите сумму</h1>

<input
  id="price"
  type="number"
  step="0.01"
  placeholder="Например: 1640.97"
/>

<button onclick="generate()">Получить картинку</button>

<img id="result" />

<script>
  const tg = window.Telegram.WebApp;
  tg.expand();

  function generate() {
    const price = document.getElementById("price").value;
    if (!price) return;

    // 👇 ЗАМЕНИ НА СВОЙ ДОМЕН
    const BACKEND_URL = "https://ТВОЙ-ДОМЕН/image";

    const img = document.getElementById("result");
    img.src = `${BACKEND_URL}?price=${price}&t=${Date.now()}`;
    img.style.display = "block";
  }
</script>

</body>
</html>

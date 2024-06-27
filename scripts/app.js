let tg = window.Telegram.WebApp;

tg.expand();

let btn = document.querySelector("a");

btn.onclick = function () {
  tg.sendData(btn.text);
};

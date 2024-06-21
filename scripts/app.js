let tg = window.Telegram.WebApp;

tg.expand();

let btn = document.querySelector("button");

btn.onclick = function () {
  let goida = document.querySelector("h1");
  goida.style.display = "none";
  tg.sendData("Goida stealed");
};

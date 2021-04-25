# Programa tarjetas electrónicas - 2021

This project is builded with Jupyter notebook in virtual env

## Requirements

You should have installed:

- Python3
- pip3
- venv -> `sudo apt-get install python3-venv -y`

## Scripts

**Bash:**

- `install.sh`: create venv, install all dependencies and launch jupyter
- `start.sh`: Launch jupyter in vevn
- `clear`: erase all venv, you can run `install.sh` after this

**Python:**

Activate venv then you can exec script python in folder `scrips`

- `change_name.py`: Normalize all names
- `web.py`: Generate all html from notebooks, and generate a list in `index.html`

## To start

Run this script:

```bash
  sudo chmod u+x install.sh
  ./install.sh
```

Otherwise:

```bash
sudo chmod u+x start.sh
  ./start.sh
```

### Alternative

```bash
python3 -m venv . #Initial a project with venv
source ./bin/activate  #activate virtual env
pip install notebook   # install notebook
jupyter notebook ./book # start a notebook
```

## Content

- Capítulo 1 Algoritmos y Diagramas de flujo
  - 1.1 Conceptos basicos y simbologia
  - 1.2 Estructura
  - 1.3 Introduccion a creacion de Diagrmas de flujo


## Softwares

- For flowchart: [drawio](https://app.diagrams.net/)

[More information to install Python3 virtual env](https://docs.python.org/3/library/venv.html)

[More information to install Jupyter Notebook](https://jupyter.org/install)
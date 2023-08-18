#!/bin/bash

# Ativar ambiente virtual (se necessário)
source venv/bin/activate

# Iniciar o cliente IRC
python modules/main.py

# Desativar ambiente virtual (opcional)
deactivate

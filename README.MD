
# Ejecución
docker-compose up

# Contenedores individuales
docker build -t csrf .
docker run --name redis -d -p 6379:6379 redis
docker run -it -p 81:80 --name csrf csrf

# Máquina local entorno virtual
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements
export FLASK_APP=app.py
flask run

# Máquina local sistema
pip3 install -r requirements
export FLASK_APP=app.py
flask run
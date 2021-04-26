
# Ejecución
docker-compose up

# Contenedores individuales
1. docker build -t csrf .
2. docker run --name redis -d -p 6379:6379 redis
3. docker run -it -p 81:80 --name csrf csrf

# Máquina local entorno virtual
1. python3 -m venv venv
2. . venv/bin/activate
3. pip3 install -r requirements
4. export FLASK_APP=app.py
5. flask run

# Máquina local sistema
1. pip3 install -r requirements
2. export FLASK_APP=app.py
3. flask run
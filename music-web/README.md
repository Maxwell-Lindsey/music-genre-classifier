# Windows:

Note: make sure to have an uploads folder, since it is in the .gitignore right now.

Open two terminals.
Back-end:

```
cd flask-server
python -m venv venv
venv\Scripts\activate
pip install flask
python server.py
http://localhost:5000/members
```

Startup the frontend:

```
cd music-web
cd client
npm start
```

backend proxy runs on localhost:5000 (configured in package.json file)

VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3
UVICORN = $(VENV)/bin/uvicorn
STREAMLIT= $(VENV)/bin/streamlit

# Need to use python 3.9 for aws lambda
$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

app: $(VENV)/bin/activate
	$(UVICORN) app:app --reload --port 8000

ws: $(VENV)/bin/activate
	$(UVICORN) ws:app --reload --port 8001

auth: $(VENV)/bin/activate
	$(UVICORN) auth:app --reload --port 8002

client: $(VENV)/bin/activate
	$(PYTHON) client.py

senti_app: $(VENV)/bin/activate
	$(UVICORN) senti_fastapi:app --reload --port 6001

senti_client: $(VENV)/bin/activate
	$(PYTHON) senti_client.py

senti_streamlit: $(VENV)/bin/activate
	$(STREAMLIT) run senti_streamlit.py --server.port 6002


clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	rm -rf $(VENV_DEV)
	rm -rf *.zip

.PHONY: login deploy

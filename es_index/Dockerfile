FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m spacy download en

# 
COPY ./*.py /code/

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8889"]

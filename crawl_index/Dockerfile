FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./*.py /code/

ENTRYPOINT ["tail", "-f", "/dev/null"]

# CMD ["python", "main.py", "JE_m2UgAAAAJ"]
#CMD ["bash"]

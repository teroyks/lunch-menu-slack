FROM python:3-alpine

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY main.py /
ADD src /src

ENV PYTHONPATH=/src
CMD python /main.py

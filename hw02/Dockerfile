FROM python:3.8-slim

RUN apt-get update
RUN apt-get install texlive-latex-base -y && apt-get install graphviz -y
RUN mkdir artifacts/

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ visualization-ast-usoltsev==0.0.1
COPY main.py main.py

CMD [ "python3", "main.py"]
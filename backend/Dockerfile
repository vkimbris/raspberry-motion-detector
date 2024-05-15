FROM python:3.10-slim

WORKDIR /backend

COPY . /backend

RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "run.sh"]
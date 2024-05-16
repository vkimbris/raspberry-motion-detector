FROM python:3.10-slim

WORKDIR /backend

COPY . /backend

RUN apt-get update && apt-get install gcc -y

RUN apt-get update && apt-get install libgl1-mesa-glx -y

RUN apt-get update && apt-get install -y libglib2.0

RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "run.sh"]
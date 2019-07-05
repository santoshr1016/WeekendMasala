FROM python:3
WORKDIR /usr/src/app
COPY requirement.txt .
RUN pip install --no-cache -r requirement.txt
COPY . .
CMD ["python", "app.py"]

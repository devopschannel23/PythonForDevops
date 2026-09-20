FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN pip install debugpy
CMD ["python", "-Xfrozen_modules=off", "app.py"]
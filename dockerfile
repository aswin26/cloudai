FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY data_tool.py .

COPY sample_data/ ./sample_data/

ENTRYPOINT ["python","data_tool.py"]


CMD []


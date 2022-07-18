FROM python:3.10-slim
ENV PYTHONPATH "${PYTHONPATH}/code"


RUN pip install --upgrade pip && pip install pip-tools
COPY requirements /tmp/pip-tmp/requirements
RUN pip-sync /tmp/pip-tmp/requirements/requirements.txt && rm -rf /tmp/pip-tmp

COPY src /app

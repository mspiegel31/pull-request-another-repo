FROM python:3.10-slim
ENV PYTHONPATH "${PYTHONPATH}/code"

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install pip-tools
COPY requirements /tmp/pip-tmp/requirements
RUN pip-sync /tmp/pip-tmp/requirements/requirements.txt && rm -rf /tmp/pip-tmp

WORKDIR /app
COPY pr_another_repo/ pr_another_repo/
COPY main.py .
COPY action.yml .

ENTRYPOINT [ "python", "/app/main.py" ]

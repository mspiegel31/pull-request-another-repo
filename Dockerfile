FROM segment/chamber:2 AS chamber

FROM python:3.10-slim

ARG REQUIREMENTS="requirements/requirements.txt"

# install requirements
RUN pip install --upgrade pip && pip install pip-tools
COPY requirements/ requirements/
RUN pip-sync ${REQUIREMENTS}

WORKDIR /code/
COPY . /code/
ENV PYTHONPATH "${PYTHONPATH}/code"

ENTRYPOINT [ "python", "main.py" ]

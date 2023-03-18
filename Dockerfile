FROM python:3.9

# Install poetry
WORKDIR /workspace
RUN pip install poetry
RUN poetry shell

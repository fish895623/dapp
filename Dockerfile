FROM python:3.9

# Install poetry
WORKDIR /workspace
COPY ./ /workspace
RUN python3 -m pip install --user poetry

RUN /root/.local/bin/poetry install
# RUN /root/.local/bin/poetry run python3 manage.py migrate
CMD /root/.local/bin/poetry run python3 manage.py runserver '0.0.0.0:8000'

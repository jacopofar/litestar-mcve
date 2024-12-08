FROM python:3.12
# copy uv as is
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ADD . /opt/breakme
WORKDIR /opt/breakme
RUN uv sync
ENV VIRTUALENV=/opt/breakme/.venv
ENV PATH=$VIRTUALENV/bin:$PATH

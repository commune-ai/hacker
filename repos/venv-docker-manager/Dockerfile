
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python"]

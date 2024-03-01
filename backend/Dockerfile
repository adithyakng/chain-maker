FROM python:3.12-slim
RUN pip install --upgrade pip

WORKDIR /

COPY ./ /app/backend

# Create environment
RUN python3 -m pip install -r /app/backend/requirements.txt

WORKDIR /app/backend

CMD ["sh","entrypoint.sh"]
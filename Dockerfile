# 1
FROM python:3.13-slim AS builder
 
RUN mkdir /app
 
WORKDIR /app
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
RUN pip install --upgrade pip 
 
COPY requirements.txt /app/
 
RUN pip install --no-cache-dir -r requirements.txt

# 2
FROM python:3.13-slim
 
RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app
 
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
 
WORKDIR /app
 
COPY --chown=appuser:appuser . .
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
USER appuser
 
EXPOSE 8010 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
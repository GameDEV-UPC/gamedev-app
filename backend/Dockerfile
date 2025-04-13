# Imagen base con Python
FROM python:3.11-slim

WORKDIR /app

COPY ./backend/app/requirements.txt .


# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de la API
EXPOSE 8000

# Comando para correr la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

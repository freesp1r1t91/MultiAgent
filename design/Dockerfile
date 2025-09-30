# Imagen base
FROM python:3.13-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements y hacer install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY src/ ./src

# Exponer puerto
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

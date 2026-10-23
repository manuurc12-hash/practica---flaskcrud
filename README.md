# Flask Contacts

## Ejecutar con Docker Compose

1. Copia `.env.example` a `.env` y reemplaza los valores de ejemplo, especialmente las contrasenas y `SECRET_KEY`.
2. Desde esta carpeta, construye e inicia los servicios:

   ```sh
   docker compose up --build
   ```

3. Abre <http://localhost:8080>.

Compose inicia Flask con Gunicorn y MySQL. La tabla se crea desde `sql/db.sql` al inicializar MySQL por primera vez; los datos se conservan en el volumen `mysql_data`.

Para detener los servicios, usa `docker compose down`. Esto conserva los datos. `docker compose down -v` tambien elimina el volumen de MySQL y todos los contactos guardados.

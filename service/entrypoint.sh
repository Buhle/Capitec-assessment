#!/bin/sh
set -e

# Wait for DB availability if requested (simple loop)
if [ "${WAIT_FOR_DB:-0}" = "1" ] || [ "${WAIT_FOR_DB}" = "true" ]; then
  echo "Waiting for database to become available..."
  # Simple Python-based check using Django DB connections
  python - <<'PY'
import os, sys, time
from django.db import connections
from django.db.utils import OperationalError

max_wait = int(os.getenv('DB_WAIT_SECONDS', '30'))
for _ in range(max_wait):
    try:
        connections['default'].introspection.table_names()
        print('Database available')
        break
    except Exception:
        time.sleep(1)
else:
    print('Timed out waiting for database')
    sys.exit(1)
PY
fi

# Run migrations if requested
if [ "${RUN_MIGRATIONS:-0}" = "1" ] || [ "${RUN_MIGRATIONS}" = "true" ]; then
  echo "Running migrations..."
  python manage.py migrate --noinput
fi

# Collect static files if requested
if [ "${COLLECT_STATIC:-0}" = "1" ] || [ "${COLLECT_STATIC}" = "true" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
fi

exec "$@"

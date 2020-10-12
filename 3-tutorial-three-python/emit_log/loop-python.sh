for i in {1..15}; do python /app/emit_log.py "Log emit message ($i / 15)"; sleep 2; done
echo "[x] Closing task service"
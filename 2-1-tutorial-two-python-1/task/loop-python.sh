for i in {1..15}; do python /app/new_task.py "10 second task ($i / 15).........."; sleep 2; done
echo "[x] Closing task service"
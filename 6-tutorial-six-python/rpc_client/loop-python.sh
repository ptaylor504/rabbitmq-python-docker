for i in {1..5};
do python /app/rpc_client.py "($i / 5)";
sleep 4;
done
echo "[x] Closing log emit service"
for i in {1..5};
do python /app/emit_log_topic.py "kern.critical" "A critical kernel error ($i / 5)";
sleep 1;
python /app/emit_log_topic.py "hello.world" "Hello World!! ($i / 5)";
sleep 1;
python /app/emit_log_topic.py "hello.critical" "An urgent HELLO!!! ($i / 5)";
sleep 1;
done
echo "[x] Closing log emit service"
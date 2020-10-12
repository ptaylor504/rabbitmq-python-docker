for i in {1..15};
do python /app/emit_log_direct.py info "This in an information log ($i / 15)";
python /app/emit_log_direct.py warning "This is a warning log ($i / 15)";
python /app/emit_log_direct.py error "This is an error log ($i / 15)";
sleep 2;
done
echo "[x] Closing log emit service"
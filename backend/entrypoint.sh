if [ "${CHAIN_MAKER_BACKEND_ENV}" = "production" ]; then
    flask run --host=0.0.0.0 --debug
else
    python main.py
fi

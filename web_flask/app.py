from . import create_app, configure_db

app = create_app()
configure_db(app)  # Call the configure_db function

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
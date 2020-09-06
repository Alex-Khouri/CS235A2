from repository import *

app = create_app()

if __name__ == "__main__":
	app.run(host='localhost', port=8080)
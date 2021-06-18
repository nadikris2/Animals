from sqlalchemy.sql.functions import user
from venv import create_app
from venv.models import User
from sqlalchemy import event

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
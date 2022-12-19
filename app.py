
from dotenv import load_dotenv
from app import *

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
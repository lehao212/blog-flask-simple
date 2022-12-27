
from dotenv import load_dotenv
from app import *
import os

if __name__ == '__main__':
    load_dotenv()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port, debug=True)

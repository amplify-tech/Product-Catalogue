# Product-Catalogue

Python Django  based  RESTful API


# Setup Instructions

git clone https://github.com/amplify-tech/Product-Catalogue.git
cd Product-Catalogue



2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate


3. Install Dependencies
pip install -r requirements.txt

4. SET DATAbase config


4. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Run Server
python manage.py runserver

open in browser: http://localhost:8000/api/

there will be api for searching and creating product list

POST http://localhost:8000/api/product/
    give input to search 
POST http://localhost:8000/api/product/create/
    give input to create the product
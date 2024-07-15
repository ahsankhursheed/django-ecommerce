python3.9 -m venv env
python3.9 -m pip install -r requirements.txt

python3.9 manage.py makemigrations 
python3.9 manage.py migrate 

python3.9 manage.py collectstatic --noinput --clear


# create a virtual environment named 'venv' if it doesn't already exist

# activate the virtual environment
source env/bin/activate

echo "BUILD END"
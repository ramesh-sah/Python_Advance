# build_files.sh
pip install -r requirements.txt
sudo apt-get install libpq-dev
python3.9 manage.py collectstatic --noinput

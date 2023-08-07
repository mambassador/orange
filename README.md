# django_orange
This repository contains a simple Django blog project created for educational purposes.


### Various features

✅CACHING PROFILE PICTURE
✅User can register + login/logout
✅Admin panel with functionality
✅ Feedback form with the admin (in the console)
✅Templates with styling
✅User can create posts (login required)
✅User can publish posts or clean them up (user can publish them later)
✅User can change his posts
✅Anonymous users can post comments
✅Comments are moderated before publication
✅ There is a page with a list of all posts
✅There is a page with a list of user posts
✅There is a post page
✅ There is a public profile page
✅ There is a profile in which you can change your data
✅Pagination of posts and comments
✅The post has a title, a short description, a picture  and a full description
✅The comment has a username and text
✅The administrator receives a notification by mail about a new post or comment (to the console)
✅The user is notified about a new comment under the post with a link to the post (console) 
✅Optimization of requests to the database
✅Fixtures loremipsum


### Setting up the project
- First you need to create virtual environment and install all dependencies:
```bash
python -m venv .venv  # creates new virtual environment
```

```bash
pip install -r requirements.txt  # installs all dependencies
```

```bash
source .venv/bin/activate  # activates your virtual environment
```

- Add SECRET_KEY to your environment variables:
```bash
export SECRET_KEY='$$$ My Secret Key $$$'  # add your secret key
```

- Migrate to set your database to actual project data structure:
```bash
./manage.py makemigrations
```
```bash
./manage.py migrate
```

- You can generate mock data for application with custom management command:
```bash
./manage.py create_mock_data 
 ```
- Deletion all mock data with command:
```bash
./manage.py delete_all_data
```
- Create superuser to get access to django admin panel
```bash
./manage.py createsuperuser
```
- You can also use fixtures from fixtures.json file to load data to your database including superuser with commands:

```bash
python manage.py loaddata fixtures.json
```
- Run project:
```bash
./manage.py runserver 
```
- Go to http://127.0.0.1:8000/ to use the app



#### Usage

1. Clone this project repository to your destination folder
2. Create a virtual environment inside your project folder with command: python3 -m venv .venv
3. Activate your new virtual environment with command: source .venv/bin/activate
4. Install dependencies with command: pip install -r requirements.txt
5. Add your secret key to your virtual environment with command: export SECRET_KEY='your secret key' 
6. Run the application with command: python3 manage.py runserver
7. Go to http://localhost:8000 to see results

#### Used Python 3.10.6
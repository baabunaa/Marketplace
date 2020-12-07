# Marketplace

Marketplace is a website, where people have a chance to post different things to sell
and others are able to choose and buy different staff. It is like an online store,
where user can find new or also used items. User can choose from several categories
or search the specific product by name. Each post has a picture, price, description,
publish date and contact information of the seller. User should register and login to put
something on the website.

## Installation

The first thing to do is to clone the repository:

```bash
$git clone https://github.com/baabunaa/Marketplace.git
$cd Marketplace/src
```

Then, create the virtual environment and activate

```bash
~/Marketplace/src$ mkvirtualenv my_django_environment
~/Marketplace/src$ source my_django_environment/bin/activate
```

Now install the requirements

```bash
(my-project-env)~/Marketplace/src$ pip3 install -r requirements.txt
```

You are ready to run the website

```bash
(my-project-env)~/Marketplace/src$ python manage.py runserver
```

Open http://127.0.0.1:8000/ and enjoy the website :)

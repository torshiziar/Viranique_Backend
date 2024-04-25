# Angizeh-Platfrom-v2

## **Introduction**

This is a private platform under right of ***Angizeh Negar Khavaran Co.*** only products that are produced in ***Angizeh
Negar Khavaran*** can integerate with it. Tested on ***ubuntu 20.04 LTS*** with the following configs :

- CPU: 2 core 2.4 GHz
- RAM: 3 GB

**Web frameworks:**

* Django==4.0.1
* djangorestframework==3.13.1

**Protocols:**

* MQTT
* WSS
* HTTPS

**Brokers and Web Servers:**

* Mosquitto
* Channels
* Nginx

**Databases:**

* PostgreSQL
* InfluxDB
* Redis

To submit bug reports and feature suggestions, or track changes:

* https://github.com/Viranique/Angizeh-Platfrom-v2/issues

## **Requirements**

All requirement libraries and packages used in python enviroment are available in Angizeh-Platfrom-v2/requirements.txt

## **Translation**

### Install Requirements : 
- Linux :
    - apt install gettext
- Windows:
    - gettext v0.15 or higher
    
### Configuration
Make Translation file through the locale folder : 
```python
# settings.py

LOCALE_PATH = (os.path.join(BASE_DIR, "locale"),)
```
Define available languages : 
```python
# settings.py

from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'fa'
LANGUAGES = [
    ('fa', _('Farsi')),
    ('en', _('English')),
]
```
Generate .po file : 
```commandline
> django-admin makemessages -l fa -i venv
```
Compile the translations : 
```commandline
> django-admin compilemessages
```

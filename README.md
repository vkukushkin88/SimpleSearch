
# Simple Search server

**Table of Contents**
 - [Installation steps](#installation-steps)
 - [Short description](#short-description)


## **Installation steps**

**The steps below assume you are using Ubuntu 16.04.**

1. [Install system requirements](#install-system-requirements)
2. [Clone this repository](#clone-this-repository)
3. [Create a virtualenv](#create-a-virtualenv)
4. [Install project dependencies](#install-project-dependencies)
5. [Run project under supervisord](#run-project-under-supervisord)



### Install system requirements

The project requires python 3.6.

Installation sequence:
```
$ sudo add-apt-repository ppa:fkrull/deadsnakes
$ sudo apt-get update
$ sudo apt-get install python3.6 python3.6-dev
```

Make sure you have installed the package - **python3.6-dev**.
This package is needed to compile the project dependencies.

Install other requirements:
```
$ sudo apt-get install libmysqlclient-dev build-essential libssl-dev libffi-dev libjpeg-dev
```


### Clone this repository

```
$ sudo mkdir -p /opt/simple_search
$ sudo chown ubuntu:ubuntu /opt/simple_search
$ cd /opt/simple_search
$ git clone git@github.com:vkukushkin88/SimpleSearch.git .
```

To create instance specific project's settings, run:
```
$ touch config/local.ini
```
and override the settings of what you need.


### Install project

It is very simple, just run:

```
$ make install
```

### Open project

Open in browse `index.html` page and have fun!

## **Short Description**

 - Project is created as simple full text search engine based on Flask + Trie
 - User can add text messages and do search through them.
 
##### Start server

```
$ python wsgi.py
```

##### Add new record by curl

```
$ curl -X POST localhost:8080/add/ -H "Content-Type: application/json" -d '{"content": "Mario Party 4"}'
```

##### Do search by curl

```
$ curl localhost:8080/search/?query=mario%20party
```

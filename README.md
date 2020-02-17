# Flask-Neo4j-Driver

Flask-Neo4j-Driver is a flask extension for the official neo4j python driver.

## Introduction

Flask-Neo4j-Driver provides the simplest possible interface to neo4j using their official driver.

Flask-Neo4j-Driver does provide a convenient 'run' method to avoid the 'with session' blocks but still allows a developer to obtain the driver session or driver directly if they prefer that approach.

## Installation

To install, use:

```bash
pip install git+https://github.com/deanwetherby/flask-neo4j-driver.git
```

### Configuration

Flask-Neo4j-Driver expects the following environment variables to be set in the flask application configuration.

| Environment Variable | Description | Default |
|----------------------|-------------|---------|
| NEO4J_URI | Neo4J URI | bolt://localhost:7687 |
| NEO4J_USER | Username | neo4j |
| NEO4J_PASS | Password | neo4j |

### Application Factory

```python
# application/__init__.py

from flask import Flask
from flask_neo4j_driver import Neo4jDriver

driver = Neo4jDriver()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    driver.init_app(app)
```

## Usage

```python
# run method with default params dictionary
statement = "MATCH (n) RETURN n"
result = driver.run(statement)
for record in result:
    print(record)
```
```python
# run method with params
statement = "CREATE (u:User {'name':$name})"
result = driver.run(statement, params={'name':'Bob'})
for record in result:
    print(record)
```
```python
# using neo4j.Session
with driver.session() as session:
    result = session.run("MATCH (n) RETURN n")
    for record in result:
        print(record)
```

## Tests

Tests assume you have a running neo4j instance either on your host or in a docker container.

Tests also assume default configurations for uri and authentication.

```bash
python -m unittest tests.test_flask_neo4j_flask
....
----------------------------------------------------------------------
Ran 4 tests in 0.108s

OK
```

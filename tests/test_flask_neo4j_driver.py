import unittest
import warnings

from flask import Flask
from flask_neo4j_driver import Neo4jDriver
import neo4j


class FlaskNeo4jDriverTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ImportWarning)
        self.app = Flask(__name__)
        self.context = self.app.test_request_context('/')
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_app(self):
        driver = Neo4jDriver(self.app)
        self.assertIsInstance(driver.app, Flask)
        self.assertIsNotNone(driver.app)

    def test_session(self):
        driver = Neo4jDriver(self.app)
        statement = "MATCH (n) RETURN n"
        with driver.session() as session:
            self.assertIsInstance(session, neo4j.Session)
            result = session.run(statement)
            self.assertIsInstance(result, neo4j.BoltStatementResult)
            for record in result:
                self.assertIsInstance(record, neo4j.Record)

    def test_run(self):
        driver = Neo4jDriver(self.app)
        statement = "MATCH (n) RETURN n"
        params = {}
        result = driver.run(statement, params)
        self.assertIsInstance(result, neo4j.BoltStatementResult)
        for record in result:
            self.assertIsInstance(record, neo4j.Record)

    def test_run_with_default_params(self):
        driver = Neo4jDriver(self.app)
        statement = "MATCH (n) RETURN n"
        result = driver.run(statement)
        self.assertIsInstance(result, neo4j.BoltStatementResult)
        for record in result:
            self.assertIsInstance(record, neo4j.Record)

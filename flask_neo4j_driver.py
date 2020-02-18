from neo4j import GraphDatabase
from flask import current_app, _app_ctx_stack


class Neo4jDriver(object):

    APP_CTX_NAME = 'neo4j_driver'

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('NEO4J_URI', 'bolt://localhost:7687')
        app.config.setdefault('NEO4J_USERNAME', 'neo4j')
        app.config.setdefault('NEO4J_PASSWORD', 'neo4j')
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, self.APP_CTX_NAME):
            ctx.neo4j_driver.close()

    def create_driver(self):
        uri = current_app.config['NEO4J_URI']
        username = current_app.config['NEO4J_USERNAME']
        password = current_app.config['NEO4J_PASSWORD']
        return GraphDatabase.driver(uri,
                                    auth=(username, password),
                                    encrypted=False)

    @property
    def driver(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, self.APP_CTX_NAME):
                ctx.neo4j_driver = self.create_driver()
            return ctx.neo4j_driver

    def session(self):
        return self.driver.session()

    def run(self, statement, params={}):
        with self.session() as session:
            result = session.run(statement, params)
            return result

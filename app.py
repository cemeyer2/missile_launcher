import os

import cherrypy
from mako.lookup import TemplateLookup

from armageddon import Armageddon


USERS = {'coreapi': 'coreapi'}


def validate_password(realm, username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False


conf = {
    '/': {
        'tools.auth_basic.on': True,
        'tools.auth_basic.realm': 'missile launcher',
        'tools.auth_basic.checkpassword': validate_password,
        'tools.staticdir.root': os.path.dirname(os.path.realpath(__file__))
    },
    '/images': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'images'
    }
}

armageddon = Armageddon()

lookup = TemplateLookup(directories=['templates'])

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.server.socket_port = 80


class MissileLauncher:
    @cherrypy.expose
    def index(self):
        tmpl = lookup.get_template("index.html")
        return tmpl.render()

    @cherrypy.expose
    def left(self):
        armageddon.send_move(armageddon.LEFT)

    @cherrypy.expose
    def right(self):
        armageddon.send_move(armageddon.RIGHT)

    @cherrypy.expose
    def up(self):
        armageddon.send_move(armageddon.UP)

    @cherrypy.expose
    def down(self):
        armageddon.send_move(armageddon.DOWN)

    @cherrypy.expose
    def fire(self):
        armageddon.send_move(armageddon.FIRE, 3)


if __name__ == '__main__':
    cherrypy.quickstart(MissileLauncher(), '/', conf)
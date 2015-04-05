import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
from armageddon import Armageddon

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
    cherrypy.quickstart(MissileLauncher())
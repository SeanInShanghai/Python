import web

render = web.template.render('templates/')

# urls = ("/.*", "hello")
urls = ('/', "hello",
        '/show', 'show',
        '/database', 'database')

app = web.application(urls, globals())

db = web.database(dbn='mysql', user='root', pw='123456', db='webpytest')

class hello:
    # def GET(self):
    def GET(self, name):
        # name = 'Bod'
        return render.helloworld(name)
        # return 'Hello, world china!'
        
        # i = web.input(name=None)
        # return render.helloworld(i.name)

class show:
    def GET(self):
        return  "show"


class database:
    def GET(self):
        if db is not None:
            return "database connect"
        else:
            return "datbase operation"

if __name__ == "__main__":
    app.run()

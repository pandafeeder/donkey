# donkey
static site generator using Django

The idea is pretty simple. Use Django's buit-in Client() to dynamicly generate client site html response based on the your Django template and your content html. Then save the generated html files into a generated directory with sub dirctories named by your content html file name, file named index.html. Then you can just use whatever server you like(Nginx, Appache, etc) to server the static folder generated.

The key of static site is that the server will server your index.html under a directory.

Your content html file could be plain html file, or better markdown file(not supported yet).

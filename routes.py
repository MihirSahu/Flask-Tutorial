#@app.route('/about/<username>') #This is a dynamic route
#def about_page(username):
#    return f'<h1>This is the about page of {username}</h1>'
#
@app.route('/') #This is a decorater; it executes before a function is executed
@app.route('/home') #Add another route that leads to the same page
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    #What we would use if we didn't have a separate db file
    #items = [
    #    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    #]

    items = Item.query.all()

    return render_template('market.html', items = items)

    #Send information into webpage by adding arguments. This is done using the Jinja framework.
    #Use double brackets {{}} in the html to call these variables
    #Use {%%} to insert logic (if statements, loops) into html
    #Template inheritance - to avoid copying and pasting a lot of html code, create a base html template that all other pages use as a base. Best practice to call it base, layout, etc.
    #   use {% extends 'base.html' %} to inherit into a page
    #   use {% block <name> %} and {% endblock %} on both inheritor and base page to add content at that place
    #Use url_for('<function name>') when using links that lead to a route you created
    #   Ex. <a class="navbar-brand" href="{{ url_for('home_page') }}">Flask Market</a>

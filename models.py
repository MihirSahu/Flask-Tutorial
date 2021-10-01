#Classes are considered individual tables in sqlalchemy
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True) #best practice to create primary key
    name = db.Column(db.String(length = 30), nullable = False, unique = True) #create a new column that holds string with a max of 30 characters, no null fields and every element has to be unique
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(length = 12), nullable = False, unique = True)
    description = db.Column(db.String(length = 1024), nullable = False)

    #Just so the database shows the name of the item when using Item.query.all()
    def __repr__(self):
        return f'Item {self.name}'
#After setting this up, go to a python terminal in the same directory as this file, import the database (db in this case) and use db.create_all(). Also import Item to be able to create items
#   from market import db, Item
#   db.create_all()
#Then you can create an item using Item() (the id is not added because it will automatically assign a primary key)
#   item1 = Item(name = "Iphone 10", price = 500, barcode = '2463746234', description = 'description')
#Then add the item into the database using db.session.add(item1)
#Then commit the data using db.session.commit()
#View items using Item.query.all()
#Loop through items by using 'for item in Item.query.all()'
#Use Item.query.filter_by() to filter by item property
#To see all data in a graphical interface, download a database browser; we'll use sqlite browser

"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corvette_chevy = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
vintage_1960 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
newer_1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
begin_cor = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
not_disc = Brand.query.filter(Brand.founded == 1903,
                                      Brand.discontinued.is_(None))
not_disc = not_disc.all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
disc_or_1950 = Brand.query.filter((Brand.discontinued.isnot(None)|
                             (Brand.founded < 1950))).all()

# Get all models whose brand_name is not Chevrolet.
not_chevrolet = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    
    models = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand)

    model_year_info = models.filter(Model.year==year)
    
    for model in model_year_info.all():
        print model.name, model.brand_name, model.headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_summary =db.session.query(Model.brand_name, Model.name).filter(Model.brand_name=="brand_name")

    for summary in brand_summary.all():
        print summary.brand_name, summary.name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

#The following is returned: flask_sqlalchemy.BaseQuery object at 0x7f48ffa32ad0>
#This is the object's location.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

#An association table helps us when defining relationships in a database.
#The primary and foriegn keys are used to show how categories are connected.
#Without this, it would be difficult to maintain normalization. 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):

    # Design a function in python that takes in any string as parameter, 
    # and returns a list of objects that are brands whose name contains or is equal to the input string.

    return Brand.query.filter((Brand.name == mystr) | (Brand.name.like('%'+mystr+'%'))).all()


def get_models_between(start_year, end_year):
    
    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

    # Design a function that takes in a start year and end year (two integers), and returns a list of objects 
    # that are models with years that fall between the start year (inclusive) and end year (exclusive).


#This section was really tough! My husband gave me a little guidance here. Looking forward to going over this with Ahmad or peers.
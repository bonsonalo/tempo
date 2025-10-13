from backend.app.core.database import base
from sqlalchemy import ForeignKey, String, Column, Integer, DECIMAL, Date
from sqlalchemy.orm import relationship



class Users(base):
    __tablename__= "users"

    id= Column(Integer, primary_key=True, index= True)
    username= Column(String, unique=True)
    hashed_password= Column(String)

class Products(base):
    __tablename__= "products"

    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, unique=True)
    price= Column(DECIMAL, index=True)
    SKU= Column(String, unique=True)
    category_id= Column(Integer, ForeignKey("categories.id", ondelete= "CASCADE"), nullable=False) #nullable=Flase means a post must belong to a user; it cannot exist without one.
    category= relationship("Categories")
    supplier_id= Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"), nullable=False) # use ondelete="CASCADE" to automatically delete related records when the parent is deleted
    supplier= relationship("Suppliers")


class Categories(base):
    __tablename__= "categories"


    id= Column(Integer, primary_key=True, index=True)
    name= Column(String)


class Suppliers(base):
    __tablename__= "suppliers"

    id= Column(Integer, primary_key=True, index=True)
    name= Column(String)

class Stock(base):
    __tablename__= "stock"

    id= Column(Integer, primary_key=True, index=True)
    product_id= Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity= Column(Integer)
    movement_type= Column(String)
    date=Column(Date)
    supplier_id= Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"))
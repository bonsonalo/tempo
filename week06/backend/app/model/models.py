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

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String, unique=True)
    price= Column(DECIMAL, index=True)
    SKU= Column(String, unique=True)
    category_id= Column(Integer, ForeignKey("categories.id", ondelete= "CASCADE"), nullable=False) #nullable=Flase means a post must belong to a user; it cannot exist without one.
    category= relationship("Categories", back_populates="product")
    supplier_id= Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"), nullable=False) # use ondelete="CASCADE" to automatically delete related records when the parent is deleted
    supplier= relationship("Suppliers", back_populates="supplier_product")
    stock= relationship("Stock", back_populates="product_stock")


class Categories(base):
    __tablename__= "categories"


    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String)
    product= relationship(Products, back_populates="category")


class Suppliers(base):
    __tablename__= "suppliers"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String)
    supplier_product= relationship("Products", back_populates="supplier")
    stock= relationship("Stock", back_populates="supplier_stock")

class Stock(base):
    __tablename__= "stock"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id= Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    product_stock= relationship("Products", back_populates="stock")
    quantity= Column(Integer)
    movement_type= Column(String)
    date= Column(Date)
    supplier_id= Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"))
    supplier_stock = relationship("Suppliers", back_populates="stock")
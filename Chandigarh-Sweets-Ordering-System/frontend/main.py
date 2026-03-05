from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

app = FastAPI(title="Chandigarh Sweets API", version="1.0.0")

# CORS - Frontend connect karne ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite:///./chandigarh_sweets.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, default="")
    order_type = Column(String, default="pickup")
    total_amount = Column(Float, nullable=False)
    order_time = Column(String)
    status = Column(String, default="Pending")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_name = Column(String, nullable=False)
    product_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    item_total = Column(Float, nullable=False)
    order = relationship("Order", back_populates="items")

Base.metadata.create_all(bind=engine)

# Products seed karo
def seed_products():
    db = SessionLocal()
    if not db.query(Product).first():
        products = [
           
# ===== MAIN COURSE =====
{"id": 1, "name": "Chana", "price": 60, "category": "Main Course"},
{"id": 2, "name": "Chana Masala", "price": 100, "category": "Main Course"},
{"id": 3, "name": "Yellow Dal (Half)", "price": 60, "category": "Main Course"},
{"id": 4, "name": "Yellow Dal (Full)", "price": 100, "category": "Main Course"},
{"id": 5, "name": "Dal Makhani (Half)", "price": 70, "category": "Main Course"},
{"id": 6, "name": "Dal Makhani (Full)", "price": 120, "category": "Main Course"},
{"id": 7, "name": "Mix Veg (Half)", "price": 80, "category": "Main Course"},
{"id": 8, "name": "Mix Veg (Full)", "price": 140, "category": "Main Course"},
{"id": 9, "name": "Mix Veg Jal Vedi", "price": 150, "category": "Main Course"},
{"id": 10, "name": "Mutter Mushroom (Half)", "price": 100, "category": "Main Course"},
{"id": 11, "name": "Mutter Mushroom (Full)", "price": 180, "category": "Main Course"},
{"id": 12, "name": "Malai Kofta (Half)", "price": 100, "category": "Main Course"},
{"id": 13, "name": "Malai Kofta (Full)", "price": 180, "category": "Main Course"},
{"id": 14, "name": "Cheese Tomato (Half)", "price": 100, "category": "Main Course"},
{"id": 15, "name": "Cheese Tomato (Full)", "price": 180, "category": "Main Course"},
{"id": 16, "name": "Shahi Paneer (Half)", "price": 100, "category": "Main Course"},
{"id": 17, "name": "Shahi Paneer (Full)", "price": 180, "category": "Main Course"},
{"id": 18, "name": "Paneer Butter Masala (Half)", "price": 100, "category": "Main Course"},
{"id": 19, "name": "Paneer Butter Masala (Full)", "price": 180, "category": "Main Course"},
{"id": 20, "name": "Karahi Paneer (Half)", "price": 100, "category": "Main Course"},
{"id": 21, "name": "Karahi Paneer (Full)", "price": 180, "category": "Main Course"},
{"id": 22, "name": "Mutter Paneer (Half)", "price": 100, "category": "Main Course"},
{"id": 23, "name": "Mutter Paneer (Full)", "price": 180, "category": "Main Course"},
{"id": 24, "name": "Paneer Do Pyaza (Half)", "price": 100, "category": "Main Course"},
{"id": 25, "name": "Paneer Do Pyaza (Full)", "price": 180, "category": "Main Course"},
{"id": 26, "name": "Paneer Bhurji (Half)", "price": 120, "category": "Main Course"},
{"id": 27, "name": "Paneer Bhurji (Full)", "price": 200, "category": "Main Course"},
{"id": 28, "name": "Mushroom Masala (Half)", "price": 120, "category": "Main Course"},
{"id": 29, "name": "Mushroom Masala (Full)", "price": 200, "category": "Main Course"},
{"id": 30, "name": "Mushroom Do Pyaza (Half)", "price": 120, "category": "Main Course"},
{"id": 31, "name": "Mushroom Do Pyaza (Full)", "price": 200, "category": "Main Course"},

# ===== RICE / SIDES =====
{"id": 32, "name": "Simple Papad", "price": 15, "category": "Sides"},
{"id": 33, "name": "Masala Papad", "price": 30, "category": "Sides"},
{"id": 34, "name": "Chana Rice", "price": 60, "category": "Rice"},
{"id": 35, "name": "Plain Rice", "price": 60, "category": "Rice"},
{"id": 36, "name": "Veg Salad", "price": 60, "category": "Sides"},
{"id": 37, "name": "Mix Raita", "price": 60, "category": "Sides"},
{"id": 38, "name": "Veg Pulao", "price": 100, "category": "Rice"},
{"id": 39, "name": "Veg Fried Rice", "price": 100, "category": "Rice"},
{"id": 40, "name": "Veg Biryani", "price": 110, "category": "Rice"},
{"id": 41, "name": "Cheese Fried Rice", "price": 130, "category": "Rice"},

# ===== BEVERAGES =====
{"id": 42, "name": "Tea", "price": 15, "category": "Beverages"},
{"id": 43, "name": "Coffee", "price": 25, "category": "Beverages"},
{"id": 44, "name": "Cold Drinks / Water", "price": 20, "category": "Beverages"},
{"id": 45, "name": "Sweet Lassi", "price": 30, "category": "Beverages"},

# ===== SNACKS =====
{"id": 46, "name": "Bread Pakora (1 Pc)", "price": 20, "category": "Snacks"},
{"id": 47, "name": "Chana Samosa (1 Pc)", "price": 25, "category": "Snacks"},
{"id": 48, "name": "Chana Samosa (2 Pc)", "price": 50, "category": "Snacks"},
{"id": 49, "name": "Veg Pakora (250gm)", "price": 40, "category": "Snacks"},
{"id": 50, "name": "Chole Bhature", "price": 50, "category": "Snacks"},
{"id": 51, "name": "Paneer Pakora (250gm)", "price": 70, "category": "Snacks"},

# ===== CHINESE =====
{"id": 52, "name": "Finger Chips (Half)", "price": 50, "category": "Chinese"},
{"id": 53, "name": "Finger Chips (Full)", "price": 80, "category": "Chinese"},
{"id": 54, "name": "Spring Roll (2 Pc)", "price": 60, "category": "Chinese"},
{"id": 55, "name": "Noodles (Half)", "price": 40, "category": "Chinese"},
{"id": 56, "name": "Noodles (Full)", "price": 60, "category": "Chinese"},
{"id": 57, "name": "Garlic Noodles", "price": 80, "category": "Chinese"},
{"id": 58, "name": "Cheese Noodles", "price": 100, "category": "Chinese"},
{"id": 59, "name": "Manchurian", "price": 100, "category": "Chinese"},
{"id": 60, "name": "Cheese Chilly", "price": 150, "category": "Chinese"},
{"id": 61, "name": "Mushroom Chilly", "price": 150, "category": "Chinese"},

# ===== SOUPS =====
{"id": 62, "name": "Veg Soup", "price": 40, "category": "Soups"},
{"id": 63, "name": "Tomato Soup", "price": 40, "category": "Soups"},
{"id": 64, "name": "Veg Manchow Soup", "price": 50, "category": "Soups"},
{"id": 65, "name": "Mushroom Soup", "price": 50, "category": "Soups"},

# ===== SOUTH INDIAN =====
{"id": 66, "name": "Sambar Wada (Half)", "price": 25, "category": "South Indian"},
{"id": 67, "name": "Sambar Wada (Full)", "price": 50, "category": "South Indian"},
{"id": 68, "name": "Plain Dosa", "price": 60, "category": "South Indian"},
{"id": 69, "name": "Masala Dosa", "price": 80, "category": "South Indian"},
{"id": 70, "name": "Onion Masala Dosa", "price": 100, "category": "South Indian"},
{"id": 71, "name": "Paneer Dosa", "price": 120, "category": "South Indian"},

# ===== SWEETS =====
{"id": 72, "name": "Spongy Rasgulla (1 Pc)", "price": 25, "category": "Sweets"},
{"id": 73, "name": "Rasmalai (1 Pc)", "price": 30, "category": "Sweets"},
{"id": 74, "name": "Hot Gulab Jamun (2 Pc)", "price": 20, "category": "Sweets"},

# ===== BREADS =====
{"id": 75, "name": "Roti", "price": 8, "category": "Breads"},
{"id": 76, "name": "Butter Roti", "price": 15, "category": "Breads"},
{"id": 77, "name": "Missi Roti", "price": 20, "category": "Breads"},
{"id": 78, "name": "Lachha Paratha", "price": 25, "category": "Breads"},
{"id": 79, "name": "Naan", "price": 25, "category": "Breads"},
{"id": 80, "name": "Butter Naan", "price": 30, "category": "Breads"},
]
        for p in products:
            db.add(Product(**p))
        db.commit()
        print("✅ Products seeded!")
    db.close()

@app.get("/")
def home():
    return {"message": "Chandigarh Sweets API Running 🍬"}

@app.get("/products")
def get_products(category: Optional[str] = None):
    db = SessionLocal()
    if category:
        products = db.query(Product).filter(Product.category == category).all()
    else:
        products = db.query(Product).all()
    db.close()
    return [{"id": p.id, "name": p.name, "price": p.price, "category": p.category} for p in products]

carts: Dict[str, Dict[int, int]] = {}

@app.post("/cart/add/{product_id}")
def add_to_cart(product_id: int, quantity: int = 1, session_id: str = "default"):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    db.close()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if session_id not in carts:
        carts[session_id] = {}
    carts[session_id][product_id] = carts[session_id].get(product_id, 0) + quantity
    return {"message": f"{product.name} added"}

@app.get("/cart")
def view_cart(session_id: str = "default"):
    if session_id not in carts:
        return {"items": [], "total": 0}
    db = SessionLocal()
    items = []
    total = 0
    for product_id, qty in carts[session_id].items():
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            item_total = product.price * qty
            total += item_total
            items.append({"id": product.id, "name": product.name, "price": product.price, "quantity": qty, "total": item_total})
    db.close()
    return {"items": items, "total": total}

class OrderModel(BaseModel):
    customer_name: str
    phone: str
    address: str = ""
    order_type: str = "pickup"
    session_id: str = "default"

@app.post("/order/place")
def place_order(order: OrderModel):
    if order.session_id not in carts or not carts[order.session_id]:
        raise HTTPException(status_code=400, detail="Cart is empty")
    db = SessionLocal()
    items_data = []
    total = 0
    for product_id, qty in carts[order.session_id].items():
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            item_total = product.price * qty
            total += item_total
            items_data.append({"product_name": product.name, "product_price": product.price, "quantity": qty, "item_total": item_total})
    
    new_order = Order(customer_name=order.customer_name, phone=order.phone, address=order.address, order_type=order.order_type, total_amount=total, order_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status="Pending")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    for item in items_data:
        db.add(OrderItem(order_id=new_order.id, **item))
    db.commit()
    db.close()
    carts[order.session_id] = {}
    return {"success": True, "order_id": new_order.id, "order_number": f"CHS{new_order.id:04d}", "total_amount": total}

@app.get("/admin/orders")
def get_all_orders():
    db = SessionLocal()
    orders = db.query(Order).order_by(Order.id.desc()).all()
    result = []
    for order in orders:
        items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
        result.append({"id": order.id, "order_number": f"CHS{order.id:04d}", "customer_name": order.customer_name, "phone": order.phone, "total_amount": order.total_amount, "status": order.status, "order_time": order.order_time, "items": [{"name": i.product_name, "qty": i.quantity, "total": i.item_total} for i in items]})
    db.close()
    return result

@app.put("/admin/order/{order_id}/status")
def update_order_status(order_id: int, status: str):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = status
    db.commit()
    db.close()
    return {"success": True, "message": f"Order status updated to {status}"}

seed_products()
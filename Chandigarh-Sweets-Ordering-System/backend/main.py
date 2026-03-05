print("🔥 BACKEND FILE LOADED 🔥")
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

app = FastAPI(
    title="Chandigarh Sweets API",
    description="Online Ordering System for Chandigarh Sweets",
    version="1.0.0"
)

# CORS - Frontend connect karne ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= DATABASE =================
DATABASE_URL = "sqlite:///./chandigarh_sweets.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# ================= DATABASE MODELS =================
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, default="")
    image = Column(String, default="")


class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, default="")
    order_type = Column(String, default="pickup")  # pickup / delivery
    payment_method = Column(String, default="cod")  # cod / online
    total_amount = Column(Float, nullable=False)
    order_time = Column(String)
    status = Column(String, default="Pending")  # Pending / Confirmed / Preparing / Ready / Delivered
    notes = Column(String, default="")
    
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


# Create tables
Base.metadata.create_all(bind=engine)

# ================= SEED PRODUCTS =================
def seed_products():
    db = SessionLocal()
    existing = db.query(Product).first()
    
    if not existing:
        products_data = [
        

# ===== MAIN COURSE =====
{"id": 1, "name": "Chana", "price": 60, "category": "Main Course", "image": "images/chana.jpg"},
{"id": 2, "name": "Chana Masala", "price": 100, "category": "Main Course", "image": "images/chanamasala.jpg"},
{"id": 3, "name": "Yellow Dal (Half)", "price": 60, "category": "Main Course", "image": "images/yellowdal.jpg"},
{"id": 4, "name": "Yellow Dal (Full)", "price": 100, "category": "Main Course","image": "images/yellowdal.jpg"},
{"id": 5, "name": "Dal Makhani (Half)", "price": 70, "category": "Main Course", "image": "images/dalmakhani.jpg"},
{"id": 6, "name": "Dal Makhani (Full)", "price": 120, "category": "Main Course", "image": "images/dalmakhani.jpg"},
{"id": 7, "name": "Mix Veg (Half)", "price": 80, "category": "Main Course", "image": "images/mixveg.jpg"},
{"id": 8, "name": "Mix Veg (Full)", "price": 140, "category": "Main Course", "image": "images/mixveg.jpg"},
{"id": 9, "name": "Mix Veg Jal Vedi", "price": 150, "category": "Main Course", "image": "images/mixvegjalvedi.jpg"},
{"id": 10, "name": "Mutter Mushroom (Half)", "price": 100, "category": "Main Course", "image": "images/muttermushroom.jpg"},
{"id": 11, "name": "Mutter Mushroom (Full)", "price": 180, "category": "Main Course", "image": "images/muttermushroom.jpg"},
{"id": 12, "name": "Malai Kofta (Half)", "price": 100, "category": "Main Course", "image": "images/malaikofta.jpg"},
{"id": 13, "name": "Malai Kofta (Full)", "price": 180, "category": "Main Course", "image": "images/malaikofta.jpg"},
{"id": 14, "name": "Cheese Tomato (Half)", "price": 100, "category": "Main Course", "image": "images/cheesetomato.jpg"},
{"id": 15, "name": "Cheese Tomato (Full)", "price": 180, "category": "Main Course", "image": "images/cheesetomato.jpg"},
{"id": 16, "name": "Shahi Paneer (Half)", "price": 100, "category": "Main Course", "image": "images/shahipaneer.jpg"},
{"id": 17, "name": "Shahi Paneer (Full)", "price": 180, "category": "Main Course", "image": "images/shahipaneer.jpg"},
{"id": 18, "name": "Paneer Butter Masala (Half)", "price": 100, "category": "Main Course", "image": "images/PaneerButterMasala.jpg"},
{"id": 19, "name": "Paneer Butter Masala (Full)", "price": 180, "category": "Main Course", "image": "images/PaneerButterMasala.jpg"},
{"id": 20, "name": "Karahi Paneer (Half)", "price": 100, "category": "Main Course",	"image":"images/karahipaneer.jpg"},
{"id": 21,	"name":"Karahi Paneer (Full)",	"price":180,	"category":"Main Course",	"image":"images/karahipaneer.jpg"},
{"id": 22,	"name":"Mutter Paneer (Half)",	"price":100,	"category":"Main Course",	"image":"images/mutterpaneer.jpg"},
{"id": 23,	"name":"Mutter Paneer (Full)",	"price":180,	"category":"Main Course",	"image":"images/mutterpaneer.jpg"},
{"id": 24, "name": "Paneer Do Pyaza (Half)", "price": 100, "category": "Main Course", "image": "images/paneerdopyaza.jpg"},
{"id": 25, "name": "Paneer Do Pyaza (Full)", "price": 180, "category": "Main Course", "image": "images/paneerdopyaza.jpg"},
{"id": 26, "name": "Paneer Bhurji (Half)", "price": 120, "category": "Main Course", "image": "images/paneerbhurji.jpg"},
{"id": 27, "name": "Paneer Bhurji (Full)", "price": 200, "category": "Main Course", "image": "images/paneerbhurji.jpg"},
{"id": 28, "name": "Mushroom Masala (Half)", "price": 120, "category": "Main Course", "image": "images/mushroommasala.jpg"},
{"id": 29, "name": "Mushroom Masala (Full)", "price": 200, "category": "Main Course",	"image":"images/mushroommasala.jpg"},
{"id": 30, "name": "Mushroom Do Pyaza (Half)",	"price":120,	"category":"Main Course",	"image":"images/mushroomdopyaza.jpg"},
{"id": 31,	"name":"Mushroom Do Pyaza (Full)",	"price":200,	"category":"Main Course",	"image":"images/mushroomdopyaza.jpg"},

# ===== RICE / SIDES =====
{"id": 32, "name": "Simple Papad", "price": 15, "category": "Sides", "image": "images/simplepapad.jpg"},
{"id": 33, "name": "Masala Papad", "price": 30, "category": "Sides", "image": "images/masalapapad.jpg"},
{"id": 34, "name": "Chana Rice", "price": 60, "category": "Rice", "image": "images/chanarice.jpg"},
{"id": 35, "name": "Plain Rice", "price": 60, "category": "Rice", "image": "images/plainrice.jpg"},
{"id": 36, "name": "Veg Salad", "price": 60, "category": "Sides", "image": "images/vegsalad.jpg"},
{"id": 37, "name": "Mix Raita", "price": 60, "category": "Sides", "image": "images/mixraita.jpg"},
{"id": 38, "name": "Veg Pulao", "price": 100, "category": "Rice",	"image":"images/vegpulao.jpg"},
{"id": 39, "name": "Veg Fried Rice", "price": 100, "category": "Rice",	"image":"images/vegfriedrice.jpg"},
{"id": 40, "name": "Veg Biryani", "price": 110, "category": "Rice", "image": "images/vegbiryani.jpg"},
{"id": 41, "name": "Cheese Fried Rice", "price": 130, "category": "Rice", "image": "images/cheesefriedrice.jpg"},

# ===== BEVERAGES =====
{"id": 42, "name": "Tea", "price": 15, "category": "Beverages", "image": "images/tea.jpg"},
{"id": 43, "name": "Coffee", "price": 25, "category": "Beverages", "image": "images/coffee.jpg"},
{"id": 44, "name": "Cold Drinks / Water", "price": 20, "category": "Beverages", "image": "images/colddrink.jpg"},
{"id": 45, "name": "Sweet Lassi", "price": 30, "category": "Beverages", "image": "images/sweetlassi.jpg"},

# ===== SNACKS =====
{"id": 46, "name": "Bread Pakora (1 Pc)", "price": 20, "category": "Snacks", "image": "images/breadpakora.jpg"},
{"id": 47, "name": "Chana Samosa (1 Pc)", "price": 25, "category": "Snacks", "image": "images/chana_samosa.jpg"},
{"id": 48, "name": "Chana Samosa (2 Pc)", "price": 50, "category": "Snacks", "image": "images/chana_samosa.jpg"},
{"id": 49, "name": "Veg Pakora (250gm)", "price": 40, "category": "Snacks", "image": "images/vegpakora.jpg"},
{"id": 50, "name": "Chole Bhature", "price": 50, "category": "Snacks",	"image":"images/cholebhature.jpg"},
{"id": 51, "name": "Paneer Pakora (250gm)", "price": 70, "category": "Snacks",	"image":"images/paneerpakora.jpg"},

# ===== CHINESE =====
{"id": 52, "name": "Finger Chips (Half)", "price": 50, "category": "Chinese", "image": "images/fingerchips.jpg"},
{"id": 53, "name": "Finger Chips (Full)", "price": 80, "category": "Chinese", "image": "images/fingerchips.jpg"},
{"id": 54, "name": "Spring Roll (2 Pc)", "price": 60, "category": "Chinese", "image": "images/springroll.jpg"},
{"id": 55, "name": "Noodles (Half)", "price": 40, "category": "Chinese", "image": "images/noodles.jpg"},
{"id": 56, "name": "Noodles (Full)", "price": 60, "category": "Chinese", "image": "images/noodles.jpg"},
{"id": 57, "name": "Garlic Noodles", "price": 80, "category": "Chinese", "image": "images/garlicnoodles.jpg"},
{"id": 58, "name": "Cheese Noodles", "price": 100, "category": "Chinese",	"image":"images/cheesenoodles.jpg"},
{"id": 59, "name": "Manchurian", "price": 100, "category": "Chinese",	"image":"images/manchurian.jpg"},
{"id": 60, "name": "Cheese Chilly", "price": 150, "category": "Chinese", "image": "images/cheesechilly.jpg"},
{"id": 61, "name": "Mushroom Chilly", "price": 150, "category": "Chinese", "image": "images/mushroomchilly.jpg"},

# ===== SOUPS =====
{"id": 62, "name": "Veg Soup", "price": 40, "category": "Soups", "image": "images/vegsoup.jpg"},
{"id": 63, "name": "Tomato Soup", "price": 40, "category": "Soups", "image": "images/tomatosoup.jpg"},
{"id": 64, "name": "Veg Manchow Soup", "price": 50, "category": "Soups", "image": "images/vegmanchowsoup.jpg"},
{"id": 65, "name": "Mushroom Soup", "price": 50, "category": "Soups",	"image":"images/mushroomsoup.jpg"},

# ===== SOUTH INDIAN =====
{"id": 66, "name": "Sambar Wada (Half)", "price": 25, "category": "South Indian", "image": "images/sambarwada.jpg"},
{"id": 67, "name": "Sambar Wada (Full)", "price": 50, "category": "South Indian", "image": "images/sambarwada.jpg"},
{"id": 68, "name": "Plain Dosa", "price": 60, "category": "South Indian", "image": "images/plaindosa.jpg"},
{"id": 69, "name": "Masala Dosa", "price": 80, "category": "South Indian",	"image":"images/masaladosa.jpg"},
{"id": 70, "name": "Onion Masala Dosa", "price": 100, "category": "South Indian",	"image":"images/onionmasaladosa.jpg"},
{"id": 71, "name": "Paneer Dosa", "price": 120, "category": "South Indian",	"image":"images/paneerdosa.jpg"},

# ===== SWEETS =====
{"id": 72, "name": "Spongy Rasgulla (1 Pc)", "price": 25, "category": "Sweets", "image": "images/spongyrasgulla.jpg"},
{"id": 73, "name": "Rasmalai (1 Pc)", "price": 30, "category": "Sweets", "image": "images/rasmalai.jpg"},
{"id": 74, "name": "Hot Gulab Jamun (2 Pc)", "price": 20, "category": "Sweets", "image": "images/hotgulabjamun.jpg"},

# ===== BREADS =====
{"id": 75, "name": "Roti", "price": 8, "category": "Breads", "image": "images/roti.jpg"},
{"id": 76, "name": "Butter Roti", "price": 15, "category": "Breads", "image": "images/butterroti.jpg"},
{"id": 77, "name": "Missi Roti", "price": 20, "category": "Breads", "image": "images/missiroti.jpg"},
{"id": 78, "name": "Lachha Paratha", "price": 25, "category": "Breads", "image": "images/lachhaparatha.jpg"},
{"id": 79, "name": "Naan", "price": 25, "category": "Breads", "image": "images/naan.jpg"},
{"id": 80, "name": "Butter Naan", "price": 30, "category": "Breads",	"image":"images/butternaan.jpg"},
]
        
        for p in products_data:
            db.add(Product(**p))
        
        db.commit()
        print("✅ Products seeded!")
    

# ================= ROOT =================
@app.get("/")
def home():
    return {"message": "Chandigarh Sweets Backend Running 🍬"}


# ================= PRODUCTS API =================
@app.get("/products")
def get_products(category: Optional[str] = None):
    db = SessionLocal()
    
    if category:
        products = db.query(Product).filter(Product.category == category).all()
    else:
        products = db.query(Product).all()
    
    db.close()

    
    return [{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "category": p.category,
        "description": p.description,
        "image": p.image
    } for p in products]


@app.get("/categories")
def get_categories():
    db = SessionLocal()
    categories = db.query(Product.category).distinct().all()
    db.close()
    return [c[0] for c in categories]


# ================= CART (Session Based) =================
# In production, use Redis or database for cart
carts: Dict[str, Dict[int, int]] = {}


@app.post("/cart/add/{product_id}")
def add_to_cart(product_id: int, quantity: int = 1, session_id: str = "default"):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    db.close()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Create cart for session if not exists
    if session_id not in carts:
        carts[session_id] = {}
    
    # Add/update item
    carts[session_id][product_id] = carts[session_id].get(product_id, 0) + quantity
    
    return {
        "message": f"{product.name} added to cart",
        "cart": carts[session_id]
    }


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
            items.append({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": qty,
                "total": item_total
            })
    
    db.close()
    
    return {"items": items, "total": total}


@app.post("/cart/clear")
def clear_cart(session_id: str = "default"):
    if session_id in carts:
        carts[session_id] = {}
    return {"message": "Cart cleared"}


# ================= ORDER =================
class OrderItemModel(BaseModel):
    product_id: int
    quantity: int


class OrderModel(BaseModel):
    customer_name: str
    phone: str
    address: str = ""
    order_type: str = "pickup"
    payment_method: str = "cod"
    notes: str = ""
    session_id: str = "default"


@app.post("/order/place")
def place_order(order: OrderModel):
    if order.session_id not in carts or not carts[order.session_id]:
        raise HTTPException(status_code=400, detail="Cart is empty")
    
    db = SessionLocal()
    
    # Calculate total
    items_data = []
    total = 0
    
    for product_id, qty in carts[order.session_id].items():
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            item_total = product.price * qty
            total += item_total
            items_data.append({
                "product_name": product.name,
                "product_price": product.price,
                "quantity": qty,
                "item_total": item_total
            })
    
    # Create order
    new_order = Order(
        customer_name=order.customer_name,
        phone=order.phone,
        address=order.address,
        order_type=order.order_type,
        payment_method=order.payment_method,
        total_amount=total,
        order_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status="Pending",
        notes=order.notes
    )
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    # Add order items
    for item in items_data:
        order_item = OrderItem(order_id=new_order.id, **item)
        db.add(order_item)
    
    db.commit()
    db.close()
    
    # Clear cart
    carts[order.session_id] = {}
    
    return {
        "success": True,
        "order_id": new_order.id,
        "order_number": f"CHS{new_order.id:04d}",
        "total_amount": total,
        "status": new_order.status,
        "message": "Order placed successfully!"
    }


# ================= ORDER TRACKING =================
@app.get("/order/{order_id}")
def track_order(order_id: int):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")
    
    items = db.query(OrderItem).filter(OrderItem.order_id == order_id).all()
    db.close()
    
    return {
        "order_id": order.id,
        "order_number": f"CHS{order.id:04d}",
        "customer_name": order.customer_name,
        "phone": order.phone,
        "address": order.address,
        "order_type": order.order_type,
        "payment_method": order.payment_method,
        "total_amount": order.total_amount,
        "status": order.status,
        "order_time": order.order_time,
        "notes": order.notes,
        "items": [{
            "name": item.product_name,
            "price": item.product_price,
            "quantity": item.quantity,
            "total": item.item_total
        } for item in items]
    }


# ================= ADMIN - GET ALL ORDERS =================
@app.get("/admin/orders")
def get_all_orders(status: Optional[str] = None):
    db = SessionLocal()
    
    if status:
        orders = db.query(Order).filter(Order.status == status).all()
    else:
        orders = db.query(Order).order_by(Order.id.desc()).all()
    
    result = []
    for order in orders:
        items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
        result.append({
            "id": order.id,
            "order_number": f"CHS{order.id:04d}",
            "customer_name": order.customer_name,
            "phone": order.phone,
            "address": order.address,
            "order_type": order.order_type,
            "total_amount": order.total_amount,
            "status": order.status,
            "order_time": order.order_time,
            "items": [{"name": i.product_name, "qty": i.quantity, "total": i.item_total} for i in items]
        })
    
    db.close()
    return result


# ================= ADMIN - UPDATE ORDER STATUS =================
@app.put("/admin/order/{order_id}/status")
def update_order_status(order_id: int, status: str):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.status = status
    db.commit()
    db.refresh(order)
    db.close()
    
    return {"success": True, "message": f"Order status updated to {status}"}


# Seed products on startup
seed_products()

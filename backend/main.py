from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for development
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ServiceItem(BaseModel):
    id: str
    title: str
    description: str
    image_url: str

class ServiceCategory(BaseModel):
    id: str
    title: str
    items: List[ServiceItem]

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    token: str
    message: str

# Data
services_data = [
    ServiceCategory(
        id="core",
        title="Core Cabinetry Services",
        items=[
            ServiceItem(id="kitchen", title="Custom Kitchen Cabinetry", description="Tailored kitchen storage solutions designed for your culinary needs.", image_url="https://placehold.co/600x400?text=Kitchen+Cabinets"),
            ServiceItem(id="bathroom", title="Bathroom Vanities", description="Elegant and functional vanities to transform your bathroom.", image_url="https://placehold.co/600x400?text=Bathroom+Vanities"),
            ServiceItem(id="built-in", title="Built-in Cabinets", description="Seamless built-ins for living rooms, offices, and libraries.", image_url="https://placehold.co/600x400?text=Built-in+Cabinets"),
            ServiceItem(id="pantry", title="Pantry Systems", description="Organized pantry storage to maximize space and efficiency.", image_url="https://placehold.co/600x400?text=Pantry+Systems"),
            ServiceItem(id="laundry", title="Laundry Room Cabinetry", description="Durable and accessible cabinetry for laundry areas.", image_url="https://placehold.co/600x400?text=Laundry+Room"),
            ServiceItem(id="mudroom", title="Mudroom Storage", description="Functional mudroom lockers and storage benches.", image_url="https://placehold.co/600x400?text=Mudroom+Storage"),
            ServiceItem(id="closet", title="Closet Cabinetry", description="High-end wood closet systems, superior to standard wire shelving.", image_url="https://placehold.co/600x400?text=Closet+Systems"),
            ServiceItem(id="garage", title="Garage Cabinets", description="Heavy-duty wood or hybrid systems for garage organization.", image_url="https://placehold.co/600x400?text=Garage+Cabinets"),
        ]
    ),
    ServiceCategory(
        id="specialized",
        title="Specialized Cabinet Work",
        items=[
            ServiceItem(id="inset-overlay", title="Inset, Overlay & Full-Overlay", description="Various construction styles to match your aesthetic preference.", image_url="https://placehold.co/600x400?text=Cabinet+Styles"),
            ServiceItem(id="frameless", title="Face-frame & Frameless", description="Traditional face-frame or modern European frameless designs.", image_url="https://placehold.co/600x400?text=Frameless+Cabinets"),
            ServiceItem(id="drawers", title="Custom Drawer Systems", description="Premium dovetail joinery and soft-close mechanisms.", image_url="https://placehold.co/600x400?text=Custom+Drawers"),
            ServiceItem(id="panels", title="Appliance Paneling", description="Custom panels for dishwashers and refrigerators for a cohesive look.", image_url="https://placehold.co/600x400?text=Appliance+Panels"),
            ServiceItem(id="floating", title="Floating Cabinets", description="Modern wall-mounted cabinets that create an airy feel.", image_url="https://placehold.co/600x400?text=Floating+Cabinets"),
            ServiceItem(id="island", title="Island Cabinetry", description="Custom center islands as the focal point of your kitchen.", image_url="https://placehold.co/600x400?text=Kitchen+Island"),
            ServiceItem(id="wine", title="Wine Storage", description="Temperature-stable and stylish wine racking and cabinetry.", image_url="https://placehold.co/600x400?text=Wine+Storage"),
            ServiceItem(id="display", title="Display Cabinets", description="Glass doors and integrated lighting to showcase your treasures.", image_url="https://placehold.co/600x400?text=Display+Cabinets"),
        ]
    )
]

# Routes
@app.get("/api/services", response_model=List[ServiceCategory])
def get_services():
    return services_data

@app.post("/api/contact")
def submit_contact(form: ContactForm):
    # In a real app, this would send an email
    print(f"Received message from {form.name} ({form.email}): {form.message}")
    return {"message": "Message received! We will contact you shortly."}

@app.post("/api/login", response_model=LoginResponse)
def login(creds: LoginRequest):
    # Hardcoded admin credentials
    if creds.username == "admin" and creds.password == "slick2024":
        return LoginResponse(token="fake-jwt-token-123", message="Login successful")
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

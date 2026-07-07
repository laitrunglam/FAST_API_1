from fastapi import FastAPI, HTTPException, Query, Path, status
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from enum import Enum
from datetime import date

app = FastAPI(title="Logistics Management API")

# --- 1. ĐỊNH NGHĨA ENUM ---

class CarrierStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"

class ShiftType(str, Enum):
    MORNING = "MORNING"
    AFTERNOON = "AFTERNOON"
    NIGHT = "NIGHT"

# --- 2. ĐỊNH NGHĨA PYDANTIC MODELS ---

class CarrierBase(BaseModel):
    code: str = Field(..., description="Mã đối tác duy nhất")
    name: str = Field(..., min_length=3, description="Tên đối tác, tối thiểu 3 ký tự")
    max_weight_capacity: int = Field(..., gt=0, description="Tải trọng tối đa, lớn hơn 0")
    status: CarrierStatus

class CarrierCreate(CarrierBase):
    pass

class CarrierUpdate(CarrierBase):
    pass

class CarrierResponse(CarrierBase):
    id: int

class ShipmentBase(BaseModel):
    carrier_id: int
    order_reference: str
    total_weight: int = Field(..., gt=0, description="Khối lượng đơn hàng, lớn hơn 0")
    dispatch_date: date
    shift: ShiftType

class ShipmentCreate(ShipmentBase):
    pass

class ShipmentResponse(ShipmentBase):
    id: int

# --- 3. DỮ LIỆU MẪU (IN-MEMORY DATABASE) ---

carriers_db = [
    {"id": 1, "code": "GHN", "name": "Giao Hang Nhanh", "max_weight_capacity": 5000, "status": CarrierStatus.ACTIVE},
    {"id": 2, "code": "GHTK", "name": "Giao Hang Tiet Kiem", "max_weight_capacity": 3000, "status": CarrierStatus.ACTIVE},
    {"id": 3, "code": "VTP", "name": "Viettel Post", "max_weight_capacity": 10000, "status": CarrierStatus.SUSPENDED}
]

shipments_db = [
    {
        "id": 1,
        "carrier_id": 1,
        "order_reference": "ORD-2026-001",
        "total_weight": 4200,
        "dispatch_date": date(2026, 7, 1),
        "shift": ShiftType.MORNING
    }
]

# --- 4. HÀM HỖ TRỢ (HELPER FUNCTIONS) ---

def get_carrier_by_id(carrier_id: int):
    for carrier in carriers_db:
        if carrier["id"] == carrier_id:
            return carrier
    return None

def check_carrier_code_exists(code: str, exclude_id: int = None):
    for carrier in carriers_db:
        if carrier["code"] == code and carrier["id"] != exclude_id:
            return True
    return False

# --- 5. API ENDPOINTS: CARRIERS ---

@app.get("/carriers", response_model=List[CarrierResponse])
def get_carriers(
    keyword: Optional[str] = Query(None, description="Tìm theo mã hoặc tên (không phân biệt hoa thường)"),
    status: Optional[CarrierStatus] = Query(None, description="Lọc theo trạng thái"),
    min_weight: Optional[int] = Query(None, description="Lọc theo tải trọng tối thiểu")
):
    result = carriers_db
    
    if keyword:
        kw = keyword.lower()
        result = [c for c in result if kw in c["code"].lower() or kw in c["name"].lower()]
        
    if status:
        result = [c for c in result if c["status"] == status]
        
    if min_weight is not None:
        result = [c for c in result if c["max_weight_capacity"] >= min_weight]
        
    return result

@app.get("/carriers/{carrier_id}", response_model=CarrierResponse)
def get_carrier(carrier_id: int = Path(...)):
    carrier = get_carrier_by_id(carrier_id)
    if not carrier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrier not found")
    return carrier

@app.post("/carriers", response_model=CarrierResponse, status_code=status.HTTP_201_CREATED)
def create_carrier(carrier: CarrierCreate):
    if check_carrier_code_exists(carrier.code):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mã đối tác (code) đã tồn tại")
    
    new_id = max([c["id"] for c in carriers_db]) + 1 if carriers_db else 1
    new_carrier = carrier.model_dump()
    new_carrier["id"] = new_id
    carriers_db.append(new_carrier)
    return new_carrier

@app.put("/carriers/{carrier_id}", response_model=CarrierResponse)
def update_carrier(carrier_update: CarrierUpdate, carrier_id: int = Path(...)):
    carrier = get_carrier_by_id(carrier_id)
    if not carrier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrier not found")
        
    if check_carrier_code_exists(carrier_update.code, exclude_id=carrier_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mã đối tác (code) đã tồn tại ở đơn vị khác")
        
    carrier.update(carrier_update.model_dump())
    return carrier

@app.delete("/carriers/{carrier_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrier(carrier_id: int = Path(...)):
    carrier = get_carrier_by_id(carrier_id)
    if not carrier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrier not found")
        
    carriers_db.remove(carrier)
    return

# --- 6. API ENDPOINTS: SHIPMENTS ---

@app.get("/shipments", response_model=List[ShipmentResponse])
def get_shipments():
    return shipments_db

@app.post("/shipments", response_model=ShipmentResponse, status_code=status.HTTP_201_CREATED)
def create_shipment(shipment: ShipmentCreate):
    # Quy tắc 1: Đối tác phải tồn tại
    carrier = get_carrier_by_id(shipment.carrier_id)
    if not carrier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrier not found")
        
    # Quy tắc 2: Trạng thái đối tác phải ACTIVE
    if carrier["status"] != CarrierStatus.ACTIVE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Đối tác vận chuyển không ở trạng thái sẵn sàng (ACTIVE)")
        
    # Quy tắc 3: Khối lượng không vượt quá năng lực (Khối lượng > 0 đã được validate ở Pydantic)
    if shipment.total_weight > carrier["max_weight_capacity"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Khối lượng chuyến hàng ({shipment.total_weight}) vượt quá tải trọng tối đa của đối tác ({carrier['max_weight_capacity']})"
        )
        
    # Quy tắc 4: Không trùng lịch điều phối (cùng dispatch_date, cùng shift)
    for existing_shipment in shipments_db:
        if (existing_shipment["carrier_id"] == shipment.carrier_id and 
            existing_shipment["dispatch_date"] == shipment.dispatch_date and 
            existing_shipment["shift"] == shipment.shift):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Đối tác này đã được xếp lịch điều phối trong ca làm việc và ngày này"
            )
            
    # Thêm chuyến hàng mới
    new_id = max([s["id"] for s in shipments_db]) + 1 if shipments_db else 1
    new_shipment = shipment.model_dump()
    new_shipment["id"] = new_id
    shipments_db.append(new_shipment)
    
    return new_shipment
# 🚖 Django Ride Pricing Module

A configurable pricing engine for ride-hailing services (Uber/Ola-like) with dynamic pricing rules.
# Results
##  Admin config
## <img width="953" alt="Screenshot 2025-06-21 171732" src="https://github.com/user-attachments/assets/801f7e87-5b8f-4da6-a684-ef9f5b5df7dd" />
## API Response
## <img width="608" alt="Screenshot 2025-06-21 171816" src="https://github.com/user-attachments/assets/9aab4ad5-12ae-47b4-8fc8-e7bdb9bc0bda" />
## Test cases
## <img width="865" alt="Screenshot 2025-06-21 173328" src="https://github.com/user-attachments/assets/d85623fd-2e88-4f25-8cfc-d92bcdadbee4" />
## Database 
## <img width="323" alt="Screenshot 2025-06-21 173514" src="https://github.com/user-attachments/assets/09f645d3-1f72-44cf-8b20-8b2fab1ad096" />


## 🚀 Features
**Multi-rule pricing**:
  - Base distance pricing
  - Additional distance rates
  - Time-based multipliers
  - Waiting charges
- **Day-specific pricing** (different rates per weekday)
- **Django Admin UI** for business team configuration
- **REST API** for real-time price calculation
- **Audit logging** of all pricing changes

## 🛠️ Installation

### Prerequisites
Prerequisites
- Python 3.7+
- Django 3.2+

### setup
bash
# Clone repository
git clone https://github.com/yourusername/django-ride-pricing.git
cd django-ride-pricing

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure database
python manage.py migrate

# Create admin user
python manage.py createsuperuser 

# Usage

## Admin Configuration

## Access admin panel at http://localhost:8000/admin

Navigate to Pricing Configs

Create pricing rules with:

Base prices per distance bracket

Additional km rates

Time multipliers (peak/off-peak)

Waiting charge thresholds
API Integration
Endpoint: GET /api/calculate-price/


# Example pricing rule for Mondays
{
  "day": 1,  # Monday
  "base_distance": 3.0,  # km
  "base_price": 90.00,   # INR
  "additional_price": 30.00  # per extra km


## Parameters:

Parameter	Type	Description	Example
distance	float	Trip distance in km	5.2
ride_time	float	Trip duration in minutes	45
waiting_time	float	Waiting time in minutes	3.5
day_of_week	int	0 (Sun) to 6 (Sat)	1

# Example Request:

# bash
curl "http://localhost:8000/api/calculate-price/?distance=5.2&ride_time=45&waiting_time=3.5&day_of_week=1"
Sample Response:

# json
{
  "price": "186.75",
  "breakdown": {
    "base_price": 80.00,
    "distance_charge": 66.00,
    "time_multiplier": 1.25,
    "waiting_charges": 10.50
  }
} 

# Testing
Run the test suite with:

# bash
python manage.py test DistancePriceCalculation
Test cases cover:

# 📂 Project Structure
.<img width="319" alt="image" src="https://github.com/user-attachments/assets/4131a23c-a2a2-4a0d-8b43-e6e28d419416" />


###  📜 License
Distributed under the MIT License. See LICENSE for more information.

### 💡 Pro Tip: Use the Django admin interface at http://localhost:8000/admin to configure pricing rules without touching code!





    





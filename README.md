# 🎯 ARMORY DB // TACTICAL DASHBOARD

**ARMORY DB** is a high-performance tactical data visualization tool built with Python and Streamlit.  
It simulates a military-grade *Heads-Up Display (HUD)* for analyzing firearm specifications, ballistics, and logistical data.

The project includes a **procedural data generator** capable of creating **500+ unique weapon variants** based on real-world templates.

---

## ⚡ Mission Capabilities (Features)

### 🖥️ Tactical HUD Interface
A dark-mode, high-contrast UI designed for clarity and aesthetics using custom CSS injection.

### 📂 Hybrid Data System
Automatically detects external datasets (`weapons_500.csv`).  
If no data is found, it initializes with a robust fallback library of 23 distinct weapons.

### 🔍 Advanced Filtering
Hierarchical drill-down filtering system:

- **Class** (e.g., Assault Rifle, Sniper)  
- **Origin** (Country)  
- **Manufacturer** (Colt, FN Herstal, etc.)  
- **Model ID** (specific variant)

### 📊 Ballistics Visualization
Visual progress bars representing:
- Muzzle Velocity  
- Effective Range  

### 🎲 Procedural Generator
Includes a script to generate synthetic datasets, creating realistic variants such as  
“M4 Carbine Tactical-7” with randomized specifications.

### 📥 Data Export
One-click CSV export of filtered datasets.

---

## 🛠️ Installation & Deployment

### **Prerequisites**
Ensure you have Python installed.

### **1. Install Dependencies**
This project requires `streamlit` and `pandas`:

```bash
pip install streamlit pandas

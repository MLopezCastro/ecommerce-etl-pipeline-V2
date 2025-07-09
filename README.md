## 🧼 ETL Ecommerce – Módulo Python

Este proyecto transforma un CSV de órdenes, aplicando limpieza, validación y cálculo de totales. Está organizado como un **proyecto ETL modular**, con estructura de carpetas, ejecución por script y testeo con `pytest`.

---

### ✅ Requisitos

* Python 3.10 o superior
* Paquetes: `pandas`

Podés instalarlos con:

```bash
pip install -r requirements.txt
```

---

### 🚀 Cómo ejecutar el pipeline

Desde la raíz del proyecto:

```bash
python scripts/run_pipeline.py
```

Esto toma los datos crudos desde `data/raw/orders.csv`, los transforma y guarda el resultado limpio en `data/output/orders_clean.csv`.

---

### 🗂️ Estructura del proyecto

```
ecommerce-etl-pipeline/
├── ecommerce_etl/        # Módulo principal con funciones ETL
│   └── transform.py
├── data/
│   ├── raw/              # Datos originales
│   │   └── orders.csv
│   └── output/           # Datos procesados
│       └── orders_clean.csv
├── scripts/              # Script de ejecución
│   └── run_pipeline.py
├── tests/                # Pruebas unitarias con pytest
│   └── test_transform.py
├── requirements.txt
├── setup.py              # (opcional) para instalación como paquete
└── README.md
```

---

### 🔄 Modo desarrollador (editable)

Si vas a trabajar en este proyecto como desarrollador, podés instalarlo en modo editable con:

```bash
pip install -e .
```

Esto te permite importar el módulo `ecommerce_etl` sin necesidad de reinstalar cada vez que lo modifiques.

---

### ⚙️ setup.py (opcional)

Si querés convertir el proyecto en un paquete instalable, agregá este archivo `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="ecommerce_etl",
    version="0.1",
    packages=find_packages(),
)
```





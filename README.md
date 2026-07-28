# Bytewise Track ML/DL Learning

My coursework, weekly assignments, and final projects from the Bytewise
Fellowship (2024 batch) Machine Learning / Deep Learning track. It starts with
Python basics and moves on to data handling, OOP, and applied ML and DL.

## Contents

| Area | Location |
|------|----------|
| Python fundamentals and OOP | `LMS.py` (library management system), `File_handling.py`, `iterators_generators.py` |
| Math utilities package | `Math/` (add, subtract, multiply, divide, modulus, exponentiation, square root) |
| Week 2 notebook | `week2.ipynb` |
| Week 4: Inventory Management | `Week4_inventoryManagement/` (OOP inventory system with CSV persistence) |
| Week 6: Classification | `Week6/Classification/weather.ipynb` (weather-type classification) |
| Week 6: Regression | `Week6/Regression/pakwheels_used_cars.ipynb` (used-car price prediction) |
| Week 10: Deep Learning | `Week 10/Bytewise_week10.ipynb` (RNN) plus write-up |
| Final project | `BWT_FinalProject/` (Streamlit plagiarism checker), `Final_project/plagarism.py` |

## Running the code

Notebooks:

```bash
pip install jupyter pandas numpy scikit-learn matplotlib seaborn tensorflow
jupyter notebook
```

Plagiarism checker (Streamlit app):

```bash
cd BWT_FinalProject
pip install -r requirements.txt
streamlit run plagiarism_checker.py
```

## License

See [LICENSE](LICENSE).

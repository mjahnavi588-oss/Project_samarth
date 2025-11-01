**Project Samarth — Crop Production & Rainfall Insights (Q&A Model)**
**Overview**

Project Samarth is a data-driven Python project that integrates agricultural crop production data with meteorological rainfall data to answer analytical questions.
It provides insights such as:

Top crops by production

Average rainfall by region

Interactive Q&A for agricultural analytics

**Project Structure**
Project_Samarth/
│
├── app.py                     
├── etl.py                     
├── qa_engine.py               
├── config.yaml               
├── requirements.txt           
├── README.md                  
│
└── data/
    ├── raw/
    │   ├── area_and_production_of_crop_2017_18.csv
    │   └── Sub_Division_IMD_2017.csv
    └── samarth.db 

   ** Install Dependencies**

pip install -r requirements.txt
python etl.py
python qa_engine.py
pip install streamlit
python -m streamlit run app.py





   

from core.firebase.client import db
from datetime import datetime, timedelta
from google.cloud.firestore_v1 import FieldFilter
import pandas as pd

collection_ref = db.collection("registers")

def add_register(data: dict):
    collection_ref.add(data)

def get_registers_by_period(period):
    year, month = period.split("-")

    year = int(year)
    month = int(month)

    start_date = datetime(day=1, month=month, year=year).strftime("%Y-%m-%d")

    if month == 12:
        month = 1
        year += 1
        end_date = datetime(day=1, month=month, year=year)
        end_date = end_date - timedelta(days=1)
        end_date = end_date.strftime("%Y-%m-%d")

    else:
        end_date = datetime(day=1, month=month + 1, year=year)
        end_date = end_date - timedelta(days=1)
        end_date = end_date.strftime("%Y-%m-%d")

    query = (
        collection_ref
        .where(filter=FieldFilter("date", ">=", f"{start_date} 00:00:00")) \
        .where(filter=FieldFilter("date", "<=", f"{end_date} 23:59:59"))
        .stream()
    )

    return sorted([doc.to_dict() for doc in query], key= lambda x: x["date"], reverse=True)

class IndicadorManager:
    def __init__(self):
        self.period = None
    
    def set_period(self, period):
        self.period = period

    def get_total_time(self, registers):
        df = pd.DataFrame(registers)
        df = pd.to_timedelta(df["actual_duration"])
        return str(df.sum())[7:]
    
    def get_biggest_session(self, registers):
        df = pd.DataFrame(registers)
        return str(pd.to_timedelta(df["actual_duration"]).max())[7:]

    
    def get_average_time(self, registers):
        df = pd.DataFrame(registers)
        focus_day = len(df["date"].unique())

        total_time = pd.to_timedelta(df["actual_duration"]).sum()
        average_time = total_time / focus_day
        average_time = str(average_time.floor("s"))[7:]
        
        return average_time

    def get_proportion_focus(self, registers):
        df = pd.DataFrame(registers)

        df = df["date"].str.split(" ").str[0]
        focus_day = len(df.unique())

        date = df[0]
        days_in_register = pd.Period(date, freq="M").days_in_month
        
        proportion = focus_day / days_in_register * 100
        return round(proportion, 1)
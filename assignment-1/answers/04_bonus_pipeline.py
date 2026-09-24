"""
Bonus +5 -- a small reporting pipeline built from Part C.

Running:
    summarise(clean(load("data/scores_raw.csv")))
reproduces the C12(a) table (mean, max, count of marks per subject) from the
raw csv in one line, with no manual steps.
"""

import numpy as np
import pandas as pd


def load(path):
    """Read the raw csv into a DataFrame."""
    return pd.read_csv(path)


def clean(df):
    """Apply the same cleaning steps used in Part C."""
    df = df.copy()

    # C5 - fix inconsistent city spelling
    df["city"] = df["city"].str.strip().str.title()

    # C6 - fill missing attendance with the column mean
    mean_attendance = df["attendance_percent"].mean()
    df["attendance_percent"] = df["attendance_percent"].fillna(mean_attendance)

    # C7 - drop exact duplicate rows, then drop rows missing marks
    df = df.drop_duplicates(keep="first")
    df = df.dropna(subset=["marks"])

    # C8 - convert exam_date to a real date type
    df["exam_date"] = pd.to_datetime(df["exam_date"])
    df["exam_month"] = df["exam_date"].dt.month
    df["exam_weekday"] = df["exam_date"].dt.day_name()

    # C10 - drop impossible marks, then add passed/grade columns
    df = df[df["marks"] <= 100]
    df["passed"] = df["marks"] >= 40
    df["grade"] = np.where(df["marks"] >= 85, "A",
                  np.where(df["marks"] >= 70, "B",
                  np.where(df["marks"] >= 40, "C", "F")))

    return df


def summarise(df):
    """Return the C12(a) table: mean, max, count of marks per subject."""
    return df.groupby("subject")["marks"].agg(["mean", "max", "count"])


if __name__ == "__main__":
    result = summarise(clean(load("data/scores_raw.csv")))
    print(result)

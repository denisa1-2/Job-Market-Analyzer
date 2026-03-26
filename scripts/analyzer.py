import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def show_basic_info(df):
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset info:")
    print(df.info())

    print("\nSummary statistics:")
    print(df.describe())

def average_salary_by_category(df):
    result = df.groupby("category")["salary"].mean()
    print("\nAverage salary by category:")
    print(result)
    return result

def jbs_by_location(df):
    result = df["location"].value_counts()
    print("\nNumber of jobs by location:")
    print(result)
    return result

def plot_salary_by_category(df):
    avg_salary = df.groupby("category")["salary"].mean()

    avg_salary.plot(kind="bar")
    plt.title("Average Salary by Category")
    plt.xlabel("Category")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.savefig("output/average_salary_category.png")
    plt.close()

def plot_jobs_by_location(df):
    jobs_count = df["location"].value_counts()

    jobs_count.plot(kind="bar")
    plt.title("Number of Jobs by Location")
    plt.xlabel("Location")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()
    plt.savefig("output/jobs_by_location.png")
    plt.close()
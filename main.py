from scripts.analyzer import (
    load_data,
    show_basic_info,
    average_salary_by_category,
    jbs_by_location,
    plot_salary_by_category,
    plot_jobs_by_location
)

def main():
    file_path = "data/jobs.csv"

    df = load_data(file_path)

    show_basic_info(df)

    average_salary_by_category(df)
    jbs_by_location(df)

    plot_salary_by_category(df)
    plot_jobs_by_location(df)

    print("\nAnalysis complete. Check the output folder for charts.")

if __name__ == "__main__":
    main()

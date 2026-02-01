import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_access_trajectory():
    # Load the ENRICHED data
    df = pd.read_csv("data/processed/enriched_fi_data.csv")
    access = df[df['indicator_code'] == 'ACC_OWNERSHIP'].copy()
    access['year'] = pd.to_datetime(access['observation_date']).dt.year
    access = access.sort_values('year')

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=access, x='year', y='value_numeric',
        marker='o', linewidth=2.5
    )

    for x, y in zip(access['year'], access['value_numeric']):
        plt.text(x, y + 1, f'{y}%', ha='center', fontweight='bold')

    plt.title("Ethiopia Account Ownership Trajectory", fontsize=14)
    plt.ylabel("Percentage of Adults (%)")
    plt.xlabel("Year")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.ylim(0, 60)

    plt.savefig("reports/figures/access_trajectory.png")
    print("Plot saved to reports/figures/access_trajectory.png")


if __name__ == "__main__":
    plot_access_trajectory()

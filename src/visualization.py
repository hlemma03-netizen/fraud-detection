import seaborn as sns
import matplotlib.pyplot as plt

def plot_class_distribution(df, target):
    sns.countplot(x=target, data=df)
    plt.title("Class Distribution")
    plt.show()


def plot_hist(df, col, title):
    sns.histplot(df[col], kde=True)
    plt.title(title)
    plt.show()


def plot_count(df, col, title):
    sns.countplot(y=col, data=df, order=df[col].value_counts().index)
    plt.title(title)
    plt.show()


def plot_fraud_by_gender(df):
    sns.countplot(x="sex", hue="class", data=df)
    plt.title("Fraud by Gender")
    plt.show()


def plot_country_fraud(df):
    df.groupby("country")["class"].mean().sort_values(ascending=False).head(10).plot(kind="bar")
    plt.title("Fraud by Country")
    plt.show()

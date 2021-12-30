import numpy as np
import matplotlib.pyplot as plt
import july
import datetime

print("GitPlot test july")


class Commit:
    create_date: datetime.datetime

    def __init__(self, create_date: datetime.datetime):
        self.create_date = create_date

    def __str__(self):
        return 'Commit(created_date=' + self.create_date.__str__() + ')'

    def __repr__(self):
        return self.__str__()


def create_fake_commit(nb_days: int):
    base = datetime.datetime.today()
    list_commit = [Commit(base - datetime.timedelta(days=x)) for x in range(nb_days)]
    list_commit.sort(key=lambda x: x.create_date, reverse=True)
    return list_commit


fake_commits = create_fake_commit(1000)


def split_by_years(commits: list):
    date_first_commit = None
    nb_chunk = -1
    chunks = []
    for commit in commits:
        if date_first_commit is None:
            date_first_commit = commit.create_date
            nb_chunk += 1
            chunks.append([])
        chunks[nb_chunk].append(commit)
        number_of_days = (date_first_commit - commit.create_date).days
        # TODO: Handle leap years.
        if number_of_days > 365:
            date_first_commit = None
    return chunks


commits_chunks = split_by_years(fake_commits)


def display_commit_by_years(commits: list):
    dates = [commit.create_date.date() for commit in commits]
    print(dates)
    data = np.random.randint(0, 15, len(dates))
    july.heatmap(
        dates,
        data,
        month_grid=True,
        title='Git Activity',
        cmap="july",
    )
    plt.show()


for commits_chunk in commits_chunks:
    display_commit_by_years(commits_chunk)

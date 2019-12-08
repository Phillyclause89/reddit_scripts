import pandas as pd

CONSTANTS = dict(
    AVG_COLUMN_NAME={0: "Average Cost Per Transaction"},
    RIGHT_GROUP_BY_COLUMNS=["uid"],
    DROP_COLUMNS=["uid", "index"],
    BY=["Total Cost"],
    COUNT_COLUMN={"Cost": "Total Transactions"},
    SUM_COLUMN={"Cost": "Total Cost"},
    LEFT_GROUP_BY_COLUMNS=["id", "Name"],
    KEEP_COLUMNS=["id", "Name", "Cost"],
    RIGHT=pd.DataFrame({
        "uid": [1, 2, 3, 4, 5, 1, 3, 5, 2, 5],
        "Cost": [99.99, 88.45, 07.15, 9.89, 56.07, 1, 50, 17.77, 32, 100]}),
    LEFT=pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "Name": ["Phil", "Yon", "Tom", "Harry", "Orion", "Nat"]}),
    HOW="left",
    LEFT_ON="id",
    RIGHT_ON="uid",
    INT_COLUMN="Total Transactions",
    NUM_COLUMN="Total Cost",
    DENOM_COLUMN="Total Transactions")


def base_merge(
        left=CONSTANTS['LEFT'],
        right=CONSTANTS['RIGHT'],
        how=CONSTANTS["HOW"],
        left_on=CONSTANTS["LEFT_ON"],
        right_on=CONSTANTS["RIGHT_ON"]):
    return left.merge(right, how=how, left_on=left_on, right_on=right_on)


def filter_by_cols(
        keep_columns=CONSTANTS["KEEP_COLUMNS"],
        frame=base_merge()):
    return frame[keep_columns]


def group_by_columns(
        gb_columns=CONSTANTS["LEFT_GROUP_BY_COLUMNS"],
        frame=filter_by_cols()):
    return frame.groupby(gb_columns)


def sum_col(
        columns=CONSTANTS["SUM_COLUMN"],
        group_by_obj=group_by_columns()):
    return group_by_obj.sum().reset_index().rename(columns=columns)


def count_col(
        columns=CONSTANTS["COUNT_COLUMN"],
        group_by_obj=group_by_columns(
            gb_columns=CONSTANTS["RIGHT_GROUP_BY_COLUMNS"],
            frame=CONSTANTS["RIGHT"]
        )):
    return group_by_obj.count().reset_index().rename(columns=columns)


def merge_sum_n_count_cols(
        left=sum_col(),
        right=count_col()):
    return base_merge(left, right)


def clean_merged_df(
        frame=merge_sum_n_count_cols(),
        drop_columns=CONSTANTS["DROP_COLUMNS"]):
    return frame.reset_index().drop(columns=drop_columns)


def convert_to_int(
        column=CONSTANTS["INT_COLUMN"]):
    return (lambda col: {c: int for c in [col]})(column)


def get_numerator_col(
        column=CONSTANTS["NUM_COLUMN"],
        frame=clean_merged_df()):
    return frame[column]


def get_denominator_col(
        column=CONSTANTS["DENOM_COLUMN"],
        frame=clean_merged_df()):
    return frame[column]


def get_avg_df(
        numerator_col=get_numerator_col(),
        denominator_col=get_denominator_col()):
    return pd.DataFrame(numerator_col.divide(denominator_col))


def merge_agg_dfs(
        left=clean_merged_df(),
        right=get_avg_df(),
        how=CONSTANTS["HOW"]):
    return left.merge(right, how=how, left_index=True, right_index=True)


def clean_agg_df(
        frame=merge_agg_dfs(),
        rename_columns=CONSTANTS["AVG_COLUMN_NAME"],
        fill_nan=0,
        round_d=2,
        as_type=convert_to_int()):
    return frame.rename(columns=rename_columns).fillna(fill_nan).round(round_d).astype(as_type)


def sorted_df(
        frame=clean_agg_df(),
        by=CONSTANTS["BY"],
        ascending=False):
    return frame.sort_values(by=by, ascending=ascending)


if __name__ == "__main__":
    print(sorted_df())

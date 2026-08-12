#calculator
import pandas as pd


def execute_query(data, query):

    operation = query["operation"]
    column = query["column"]

    if column not in data.columns:
        return (
            f"Column '{column}' not found. "
            f"Available columns: {list(data.columns)}"
        )

    filters = query.get("filters", {})

    for filter_column, values in filters.items():

        if filter_column not in data.columns:
            return (
                f"Filter column '{filter_column}' not found. "
                f"Available columns: {list(data.columns)}"
            )

        data = data[data[filter_column].isin(values)]

    if operation == "sum":

        return data[column].sum()

    elif operation == "mean":

        return data[column].mean()

    elif operation == "max":

        return data[column].max()

    elif operation == "min":

        return data[column].min()

    elif operation == "count":

        return data[column].count()

    elif operation == "ranking":

        group_by = query.get("group_by")
        aggregation = query.get("aggregation", "sum")

        if group_by:

            if group_by not in data.columns:
                return (
                    f"Group-by column '{group_by}' not found. "
                    f"Available columns: {list(data.columns)}"
                )

            grouped = (
                data
                .groupby(group_by)[column]
                .agg(aggregation)
                .reset_index()
            )

            sort_order = query.get("sort", "descending")

            grouped = grouped.sort_values(
                by=column,
                ascending=(sort_order == "ascending")
            )

            # Limit
            limit = query.get("limit")

            if limit is not None:
                grouped = grouped.head(limit)

            return grouped
        else:

            sort_order = query.get("sort", "descending")

            result = data.sort_values(
                by=column,
                ascending=(sort_order == "ascending")
            )

            limit = query.get("limit")

            if limit is not None:
                result = result.head(limit)

            return result

    else:

        return f"Operation '{operation}' is not supported yet."

if __name__ == "__main__":

    file_path = "data/Humanitarian_Data.xlsx"

    population = pd.read_excel(
        file_path,
        sheet_name="Population"
    )

    print("\nAvailable columns:")
    print(population.columns.tolist())

    test_query = {
        "operation": "mean",
        "column": "Refugees",
        "filters": {}
    }

    result = execute_query(population, test_query)

    print("\nAverage refugees:")
    print(result)

    test_query = {
        "operation": "mean",
        "column": "Refugees",
        "filters": {
            "Country of Asylum": ["India", "Nepal"]
        }
    }

    result = execute_query(population, test_query)

    print("\nAverage refugees in India and Nepal:")
    print(result)


    test_query = {
        "operation": "ranking",
        "column": "Refugees",
        "group_by": "Country of Asylum",
        "aggregation": "sum",
        "filters": {},
        "sort": "descending",
        "limit": 5
    }

    result = execute_query(population, test_query)

    print("\nTop 5 countries by total refugees:")
    print(result)
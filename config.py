from queries import filter_query, map_query, limit_query, sort_query, unique_query, regex_query


CMD_TO_EXECUTE: dict = {"filter": filter_query,
                        "unique": unique_query,
                        "limit": limit_query,
                        "regex": regex_query,
                        "sort": sort_query,
                        "map": map_query
                        }

LOG_DIR_NAME: str = "data/"

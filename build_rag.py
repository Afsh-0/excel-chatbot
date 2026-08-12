from rag import create_knowledge


FILE_PATH = "data/Humanitarian_Data.xlsx"


result = create_knowledge(FILE_PATH)

print(result)
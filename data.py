import requests
parameters = {
    "amount":10,
    "category": 27,
    "difficulty": "easy",
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()


question_data = response.json()["results"]

# question_data = [
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Israel is 7 hours ahead of New York.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Alaska is the largest state in the United States.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "There exists an island named &quot;Java&quot;.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "&quot;Mongolia&quot; was a part of the now non-existent U.S.S.R.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Toronto is the capital city of the North American country of Canada.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "California is larger than Japan.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Hungary is the only country in the world beginning with H.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "Only one country in the world starts with the letter Q.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Is Tartu the capital of Estonia?",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]

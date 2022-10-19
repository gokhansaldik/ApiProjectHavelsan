"this project is The Rick and Morty API query"

import requests

URLMrGoldenfold = "https://rickandmortyapi.com/api/character/240"
URLYellowHeadedDoctor = "https://rickandmortyapi.com/api/character/384"
URLSlippy = "https://rickandmortyapi.com/api/character/571"
URLProfessorSanchez = "https://rickandmortyapi.com/api/character/619"
URLCenobite = "https://rickandmortyapi.com/api/character/746"

resultMrGoldenfold = requests.get(URLMrGoldenfold)
resultYellowHeadedDoctor = requests.get(URLYellowHeadedDoctor)
resultSlippy = requests.get(URLSlippy)
resultProfessorSanchez = requests.get(URLProfessorSanchez)
resultCenobite = requests.get(URLCenobite)

dataMrGoldenfold = resultMrGoldenfold.json()
dataMrYellowHeadedDoctor = resultYellowHeadedDoctor.json()
dataSlippy = resultSlippy.json()
dataProfessorSanchez = resultProfessorSanchez.json()
dataCenobite = resultCenobite.json()

print(dataMrGoldenfold)
print(dataMrYellowHeadedDoctor)
print(dataSlippy)
print(dataProfessorSanchez)
print(dataCenobite)
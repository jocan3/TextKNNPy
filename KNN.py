from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import DistanceMetric
from sklearn.metrics import jaccard_similarity_score
from sklearn.metrics.pairwise import cosine_similarity
from DBCredentials import DBUser, DBPassword, DBName, DBHost
import mysql.connector
import random
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def customJaccard(x,y):
    Xvalue = [x,y]
    dist = DistanceMetric.get_metric('jaccard')
    jaccardResult = dist.pairwise(Xvalue)
    return jaccardResult[0][1]

def customCosine(x,y):
    cosResult = cosine_similarity(x,y)
    return (1-(cosResult[0] + 1)/2)

datasetRepresentationId = 24
algorithmName = 'KNN'
additionalInfo = 'No ensemble'
metricName = 'Jaccard'
k = 30
train = 75
test = 25

cnx = mysql.connector.connect(user=DBUser, password=DBPassword,
                              host=DBHost,
                              database=DBName)
cursor = cnx.cursor()
query = ("SELECT id FROM algorithm WHERE name='%s'")
cursor.execute(query % (algorithmName))
algorithmId = cursor.fetchone()
algorithmId = algorithmId[0]
cursor.close()

cursor = cnx.cursor()
query = ("SELECT id FROM metric WHERE name='%s'")
cursor.execute(query % (metricName))
metricId = cursor.fetchone()
metricId = metricId[0]
cursor.close()

cursor = cnx.cursor()
query = ("SELECT description FROM datasetrepresentation WHERE id=%i")
cursor.execute(query % (datasetRepresentationId))
datasetRepresentationDescription = cursor.fetchone()
datasetRepresentationDescription = datasetRepresentationDescription[0]
cursor.close()

description = datasetRepresentationDescription + ". Algorithm: " + algorithmName + " ("+ additionalInfo + "). Metric: " + metricName + ". K=" + str(k) + ". Train=" + str(train) + "% Test=" + str(test) + "%."

cursor = cnx.cursor()
addExperiment = ("INSERT INTO experiment(datasetRepresentation, algorithm, metric, description, status) VALUES (%i, %i, %i, '%s', '%s')")
dataExperiment = (datasetRepresentationId, algorithmId, metricId, description, "running")
cursor.execute(addExperiment % dataExperiment)
experimentId = cursor.lastrowid
cursor.close()

cnx.commit()

cursor = cnx.cursor()
query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a')")
cursor.execute(query % (datasetRepresentationId))
documents = cursor.fetchall()
cursor.close()

vectorsTrain = []
vectorsTest = []
classesTrain = []
classesTest = []
documentIdsTrain = []
documentIdsTest = []

c = 0

documentsTrain, documentsTest = train_test_split(documents, test_size=(test/100), random_state=int((random.random()*10)))
for (document) in documentsTrain:
    documentIdsTrain.append(document[0])
    vectorsTrain.append(document[3].split(','))
    classesTrain.append(document[4])
    c = c + 1

for (document) in documentsTest:
    documentIdsTest.append(document[0])
    vectorsTest.append(document[3].split(','))
    classesTest.append(document[4])
    c = c + 1


# for (document) in documents:
#     if c > 0:
#         documentIds.append(document[0])
#         vectors.append(document[3].split(','))
#         classes.append(document[4])
#     c = c + 1
#
# vectorsTrain, vectorsTest, classesTrain, classesTest, documentsTrain, documentsTest = train_test_split(vectors, classes, documentIds, test_size=(test/100), random_state=int((random.random()*10)))

# print(vectorsTrain)
# print(vectorsTest)
# print(classesTrain)
# print(classesTest)


#dist = DistanceMetric.get_metric(metricName.lower())

funcDist = None
if metricName == 'Cosine':
    funcDist = customCosine
if metricName == 'Jaccard':
    funcDist = customJaccard


neigh = KNeighborsClassifier(n_neighbors=1, metric=funcDist)
neigh.fit(vectorsTrain, classesTrain)

predictions = []
c = 0


for (vector) in vectorsTest:
    predictions.append(neigh.predict(vector))
    cursor = cnx.cursor()
    addImputation = ("INSERT INTO imputation(document, experiment, expectedClass, imputedClass) VALUES (%i, %i, '%s', '%s')")
   # print(predictions[c][0])

    dataImputation = (documentIdsTest[c], experimentId, classesTest[c], predictions[c][0])
    cursor.execute(addImputation % dataImputation)
    cursor.close()
    c = c + 1
    cnx.commit()

cursor = cnx.cursor()
updateExperiment = ("UPDATE experiment SET status='successful' WHERE id=%i")
dataUpdateExperiment = (experimentId)
cursor.execute(updateExperiment % dataUpdateExperiment)
cursor.close()
cnx.commit()
cnx.close()

# for (doc1) in documents:
#     str1 = "(" + doc1[2] + " --- "
#     for (doc2) in documents:
#         dist = funcDist(doc1[3].split(','),doc2[3].split(','))
#         str2 = str1 + doc2[2] + ") = Distance: " + str(dist)
#         print(str2)

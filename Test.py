from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import DistanceMetric
from sklearn.metrics import jaccard_similarity_score
from sklearn.metrics import mutual_info_score
from sklearn.metrics.pairwise import cosine_similarity
from DBCredentials import DBUser, DBPassword, DBName, DBHost
import mysql.connector
import random
import sys
import warnings
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)

def customJaccard(x,y):
    Xvalue = [x,y]
    dist = DistanceMetric.get_metric('jaccard')
    jaccardResult = dist.pairwise(Xvalue)
    return jaccardResult[0][1]

def customCosine(x,y):
    cosResult = cosine_similarity(x,y)
    return (1-(cosResult[0] + 1)/2)

def customKLD(x,y):
    KLResult = mutual_info_score(x,y)
    return 1-KLResult


#metricNames = ['Jaccard','Cosine']
metricNames = ['Divergence-KL','Cosine']
datasetRepresentationId = 24
algorithmName = 'KNN'
#algorithmName = 'LDA'

techniques = ["No ensemble"]
additionalInfo = 'No ensemble'
metricName = 'Jaccard'
k = 30
train = 75
test = 25

trainList = [50]
testList = [50]

k = 10
#increment = 1 #for oil test
#maxK = int(numDocuments * 0.35) # for oil test
increment = 1
maxK = 11
batch = -1


kList = []

cnx = mysql.connector.connect(user=DBUser, password=DBPassword,
                              host=DBHost,
                              database=DBName)
cnx2 = mysql.connector.connect(user=DBUser, password=DBPassword,
                              host=DBHost,
                              database=DBName)

cursorDR = cnx2.cursor()
query = ("SELECT id,description FROM datasetrepresentation WHERE active=1")
cursorDR.execute(query)
datasetRepresentationDescription = cursorDR.fetchone()

while (datasetRepresentationDescription is not None):
    datasetRepresentationId = datasetRepresentationDescription[0]
    datasetRepresentationDescription = datasetRepresentationDescription[1]

    print("Processing DR: " + datasetRepresentationDescription)
    for (metricName) in metricNames:
        print("2 " + metricName + ". Desc: " + datasetRepresentationDescription)
        if (metricName == "Jaccard" and "without TF-IDF" in datasetRepresentationDescription) or (metricName == "Divergence-KL" and "LDA" in datasetRepresentationDescription) or metricName == "Cosine":
            print("3")

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
            query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a') AND class NOT LIKE 'TEST:%%'")
            cursor.execute(query % (datasetRepresentationId))
            documents = cursor.fetchall()
            cursor.close()

            numDocuments = len(documents)

            print("Num docs = " + str(numDocuments))
            print("maxK = " + str(maxK))

            while (k < maxK):
                print("4")
                for (trainValue) in trainList:
                    print("5")
                    train = trainValue
                    test = 100 - train

                    if ("LDA" not in datasetRepresentationDescription) or ("LDA" in datasetRepresentationDescription and ("Train: "+str(train)) in datasetRepresentationDescription):

                        for (additionalInfo) in techniques:
                            print("6")
                            description = datasetRepresentationDescription + ". Algorithm: " + algorithmName + " (" + additionalInfo + "). Metric: " + metricName + ". K=" + str(
                                k) + ". Train=" + str(train) + "% Test=" + str(test) + "%."

                            # cursor = cnx.cursor()
                            # addExperiment = (
                            # "INSERT INTO experiment(datasetRepresentation, algorithm, metric, description, status, batch) VALUES (%i, %i, %i, '%s', '%s', %i)")
                            # dataExperiment = (datasetRepresentationId, algorithmId, metricId, description, "running", batch)
                            # cursor.execute(addExperiment % dataExperiment)
                            # experimentId = cursor.lastrowid
                            # cursor.close()
                            #
                            # cnx.commit()

                            vectorsTrain = []
                            vectorsTest = []
                            classesTrain = []
                            classesTest = []
                            documentIdsTrain = []
                            documentIdsTest = []

                            c = 0

                            if ("LDA" in datasetRepresentationDescription):
                                documentsTrain = documents
                                cursor = cnx.cursor()
                                query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a') AND class LIKE 'TEST:%%' LIMIT 5")
                                cursor.execute(query % (datasetRepresentationId))
                                documentsTest = cursor.fetchall()
                                cursor.close()
                            else:
                                documentsTrain, documentsTest = train_test_split(documents, test_size=(test / 100),
                                                                         random_state=int(time.time()))
                            for (document) in documentsTrain:
                                documentIdsTrain.append(document[0])
                                vectorsTrain.append(document[3].split(','))
                                classesTrain.append(document[4])
                                c = c + 1

                            for (document) in documentsTest:
                                documentIdsTest.append(document[0])
                                vectorsTest.append(document[3].split(','))
                                classesTest.append(document[4][5:])
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


                            # dist = DistanceMetric.get_metric(metricName.lower())

                            funcDist = None
                            if metricName == 'Cosine':
                                funcDist = customCosine
                            if metricName == 'Jaccard':
                                funcDist = customJaccard
                            if metricName == 'Divergence-KL':
                                funcDist = customKLD

                            neigh = KNeighborsClassifier(n_neighbors=k, metric=funcDist)

                            if (additionalInfo == "No ensemble"):
                                print("7")
                                neigh.fit(vectorsTrain, classesTrain)
                                predictions = []
                                c = 0
                                for (vector) in vectorsTest:
                                    predictions.append(neigh.predict(vector))
                                    print("Document test id: " + str(documentIdsTest[c]))
                                    print("Predicted: " + str(predictions[c][0]))
                                    # cursor = cnx.cursor()
                                    # addImputation = (
                                    #     "INSERT INTO imputation(document, experiment, expectedClass, imputedClass) VALUES (%i, %i, '%s', '%s')")
                                    # # print(predictions[c][0])
                                    #
                                    # dataImputation = (
                                    #     documentIdsTest[c], experimentId, classesTest[c], predictions[c][0])
                                    # cursor.execute(addImputation % dataImputation)
                                    # cursor.close()
                                    c = c + 1
                                    # cnx.commit()

                                # cursor = cnx.cursor()
                                # updateExperiment = ("UPDATE experiment SET status='successful' WHERE id=%i")
                                # dataUpdateExperiment = (experimentId)
                                # cursor.execute(updateExperiment % dataUpdateExperiment)
                                # cursor.close()
                                # cnx.commit()

                            if (additionalInfo == "bagging"):
                                print("8")
                                bagging = BaggingClassifier(neigh,max_samples=0.15, max_features=1.0)
                                bagging.fit(vectorsTrain, classesTrain)
                                predictions = []
                                c = 0
                                for (vector) in vectorsTest:
                                    predictions.append(bagging.predict(vector))
                                    # cursor = cnx.cursor()
                                    # addImputation = (
                                    #     "INSERT INTO imputation(document, experiment, expectedClass, imputedClass) VALUES (%i, %i, '%s', '%s')")
                                    # # print(predictions[c][0])
                                    #
                                    # dataImputation = (
                                    #     documentIdsTest[c], experimentId, classesTest[c], predictions[c][0])
                                    # cursor.execute(addImputation % dataImputation)
                                    # cursor.close()
                                    c = c + 1
                                    #cnx.commit()

                                # cursor = cnx.cursor()
                                # updateExperiment = ("UPDATE experiment SET status='successful' WHERE id=%i")
                                # dataUpdateExperiment = (experimentId)
                                # cursor.execute(updateExperiment % dataUpdateExperiment)
                                # cursor.close()
                                # cnx.commit()

                                # for (doc1) in documents:
                            #     str1 = "(" + doc1[2] + " --- "
                            #     for (doc2) in documents:
                            #         dist = funcDist(doc1[3].split(','),doc2[3].split(','))
                            #         str2 = str1 + doc2[2] + ") = Distance: " + str(dist)
                            #         print(str2)

                k = k + increment

    datasetRepresentationDescription = cursorDR.fetchone()

cnx.close()
cnx2.close()
cursorDR.close()

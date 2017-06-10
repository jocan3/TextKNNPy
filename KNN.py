from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import DistanceMetric
from sklearn.metrics import jaccard_similarity_score
from sklearn.metrics import mutual_info_score
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import entropy
from DBCredentials import DBUser, DBPassword, DBName, DBHost
from Parameters import metricNames, algorithmName, techniques, trainList, k, increment, maxK, maxSamples, batch
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

# def customKLD(x,y):
#     KLResult = mutual_info_score(x,y)
#     return 1-KLResult

#def customKLD(x,y):
#    KLResult = normalized_mutual_info_score(x,y)
 #   return 1 - KLResult

def customKLD(x,y):
    newX = [0.000001 if e == 0 else e for e in x]
    newY = [0.000001 if e == 0 else e for e in y]
    KLResult = entropy(newX,newY)
    return KLResult

original_k = k

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
        if (metricName == "Jaccard" and "without TF-IDF" in datasetRepresentationDescription) or (metricName == "Divergence-KL" and "LDA" in datasetRepresentationDescription) or metricName == "Cosine":

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

            datasetRepresentationDescriptionTest = datasetRepresentationDescription.replace("File:Train","File:Test")
            print("Test = " + datasetRepresentationDescriptionTest)
            cursor = cnx.cursor()
            query = ("SELECT id FROM datasetrepresentation where description='%s'")
            cursor.execute(query % (datasetRepresentationDescriptionTest))
            datasetRepresentationIdTest = cursor.fetchone()
            datasetRepresentationIdTest = datasetRepresentationIdTest[0]
            cursor.close()

            numDocuments = len(documents)

            k = original_k
            while (k < maxK):
                for (trainValue) in trainList:
                    #print("5")
                    train = trainValue
                    test = 100 - train

                    if (datasetRepresentationDescription and ("Train:"+str(train)) in datasetRepresentationDescription):

                        for (additionalInfo) in techniques:
                           # print("6")
                            description = datasetRepresentationDescription + ". Algorithm: " + algorithmName + " (" + additionalInfo + "). Metric: " + metricName + ". K=" + str(
                                k) + ". Train=" + str(train) + "% Test=" + str(test) + "%."

                            cursor = cnx.cursor()
                            addExperiment = (
                            "INSERT INTO experiment(datasetRepresentation, algorithm, metric, description, status, batch) VALUES (%i, %i, %i, '%s', '%s', %i)")
                            dataExperiment = (datasetRepresentationId, algorithmId, metricId, description, "running", batch)
                            cursor.execute(addExperiment % dataExperiment)
                            experimentId = cursor.lastrowid
                            cursor.close()

                            cnx.commit()

                            vectorsTrain = []
                            vectorsTest = []
                            classesTrain = []
                            classesTest = []
                            documentIdsTrain = []
                            documentIdsTest = []

                            c = 0

                            documentsTrain = documents
                            cursor = cnx.cursor()
                            query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a')")
                            cursor.execute(query % (datasetRepresentationIdTest))
                            documentsTest = cursor.fetchall()
                            cursor.close()

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

                            funcDist = None
                            if metricName == 'Cosine':
                                funcDist = customCosine
                            if metricName == 'Jaccard':
                                funcDist = customJaccard
                            if metricName == 'Divergence-KL':
                                funcDist = customKLD

                            neigh = KNeighborsClassifier(n_neighbors=k, metric=funcDist)

                            if (additionalInfo == "No ensemble"):
                                #print("7")
                                neigh.fit(vectorsTrain, classesTrain)
                                predictions = []
                                c = 0
                                for (vector) in vectorsTest:
                                    predictions.append(neigh.predict(vector))
                                    cursor = cnx.cursor()
                                    addImputation = (
                                        "INSERT INTO imputation(document, experiment, expectedClass, imputedClass) VALUES (%i, %i, '%s', '%s')")
                                    # print(predictions[c][0])
                                    dataImputation = (
                                        documentIdsTest[c], experimentId, classesTest[c], predictions[c][0])
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

                            if (additionalInfo == "bagging"):
                               # print("8")
                                bagging = BaggingClassifier(neigh,max_samples=maxSamples, max_features=1.0)
                                bagging.fit(vectorsTrain, classesTrain)
                                predictions = []
                                c = 0
                                for (vector) in vectorsTest:
                                    predictions.append(bagging.predict(vector))
                                    cursor = cnx.cursor()
                                    addImputation = (
                                        "INSERT INTO imputation(document, experiment, expectedClass, imputedClass) VALUES (%i, %i, '%s', '%s')")
                                    # print(predictions[c][0])

                                    dataImputation = (
                                        documentIdsTest[c], experimentId, classesTest[c], predictions[c][0])
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

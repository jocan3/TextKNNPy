from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import DistanceMetric
from sklearn.metrics import mutual_info_score
from sklearn.metrics.pairwise import cosine_similarity
from DBCredentials import DBUser, DBPassword, DBName, DBHost
from Parameters import Experiment,votingCombinations
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

cnx = mysql.connector.connect(user=DBUser, password=DBPassword,
                              host=DBHost,
                              database=DBName)
cnx2 = mysql.connector.connect(user=DBUser, password=DBPassword,
                              host=DBHost,
                              database=DBName)

for (combination) in votingCombinations:
    estimators = []
    documentsTrain = []
    documentsTest = []
    combClassesTrain = []
    combClassesTest = []
    combIdsTrain = []
    combIdsTest = []
    combinationDescription = ""
    combC = 0
    for (experiment) in combination:
        documentIdsTrain = []
        vectorsTrain = []
        classesTrain = []
        documentIdsTest = []
        vectorsTest = []
        classesTest = []

        cursorDR = cnx2.cursor()
        query = ("SELECT id,datasetRepresentation,algorithm,metric,description FROM experiment WHERE description LIKE '%%%s%%'")
        cursorDR.execute(query % (experiment.description))
        experimentObject = cursorDR.fetchone()

        experimentId = experimentObject[0]
        datasetRepresentationId = experimentObject[1]
        algorithmId = experimentObject[2]
        metricId = experimentObject[3]
        combinationDescription += experimentObject[4] + "+"
        k = experiment.k

        cursor = cnx.cursor()
        query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a')")
        cursor.execute(query % (datasetRepresentationId))
        documents = cursor.fetchall()
        cursor.close()

        for (document) in documents:
            documentIdsTrain.append(document[0])
            vectorsTrain.append(document[3].split(','))
            classesTrain.append(document[4])

        descriptionTest = experiment.description.split(".")[0].replace("File:Train","File:Test")

        cursorDR = cnx2.cursor()
        query = (
        "SELECT id FROM datasetrepresentation WHERE description LIKE '%%%s%%'")
        cursorDR.execute(query % (descriptionTest))
        experimentObject = cursorDR.fetchone()

        datasetRepresentationId = experimentObject[0]

        cursor = cnx.cursor()
        query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a')")
        cursor.execute(query % (datasetRepresentationId))
        documents = cursor.fetchall()
        cursor.close()

        for (document) in documents:
            documentIdsTest.append(document[0])
            vectorsTest.append(document[3].split(','))
            classesTest.append(document[4])

        funcDist = None
        if metricId == 1:
            funcDist = customCosine
        if metricId == 2:
            funcDist = customJaccard
        if metricId == 3:
            funcDist = customKLD

        neigh = KNeighborsClassifier(n_neighbors=k, metric=funcDist)
        estimators.append((combC, neigh))

        documentsTrain.append(vectorsTrain)
        documentsTest.append(vectorsTest)
        combClassesTrain.append(classesTrain)
        combClassesTest.append(classesTest)
        combIdsTrain.append(documentIdsTrain)
        combIdsTest.append(documentIdsTest)
        combinationDescription = combinationDescription + "+" + experiment.description
        combC = combC + 1



while (datasetRepresentationDescription is not None):
    datasetRepresentationId = datasetRepresentationDescription[0]
    datasetRepresentationDescription = datasetRepresentationDescription[1]

    print("Processing DR: " + datasetRepresentationDescription)
    for (metricName) in metricNames:
        #print("2 " + metricName + ". Desc: " + datasetRepresentationDescription)
        if (metricName == "Jaccard" and "without TF-IDF" in datasetRepresentationDescription) or (metricName == "Divergence-KL" and "LDA" in datasetRepresentationDescription) or metricName == "Cosine":
            #print("3")

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
            #print("Test = " + datasetRepresentationDescriptionTest)
            cursor = cnx.cursor()
            query = ("SELECT id FROM datasetrepresentation where description='%s'")
            cursor.execute(query % (datasetRepresentationDescriptionTest))
            datasetRepresentationIdTest = cursor.fetchone()
            datasetRepresentationIdTest = datasetRepresentationIdTest[0]
            cursor.close()

            numDocuments = len(documents)

           # print("Num docs = " + str(numDocuments))
            #print("maxK = " + str(maxK))
            while (k < maxK):
               # print("4")
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
                                bagging = BaggingClassifier(neigh,max_samples=0.15, max_features=1.0)
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

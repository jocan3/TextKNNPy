from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import DistanceMetric
from sklearn.metrics import mutual_info_score
from sklearn.metrics.pairwise import cosine_similarity
from Test import VotingClassifier
from DBCredentials import DBUser, DBPassword, DBName, DBHost
from Parameters import Experiment,votingCombinations,comments
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

cont = 0
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

    cursor = cnx.cursor()
    addExperiment = (
        "INSERT INTO votingexperiment(description, status) VALUES ('%s', '%s')")
    dataExperiment = (combinationDescription, "running")
    cursor.execute(addExperiment % dataExperiment)
    votingExperimentId = cursor.lastrowid
    cursor.close()
    cnx.commit()

    for (experiment) in combination:
        documentIdsTrain = []
        vectorsTrain = []
        classesTrain = []
        documentIdsTest = []
        vectorsTest = []
        classesTest = []
        print("Processing combination: " + str(cont))
        print("Processing experiment: " + experiment.description)
        cursor = cnx.cursor()
        query = ("SELECT id,datasetRepresentation,algorithm,metric,description FROM experiment WHERE description LIKE '%%%s%%' limit 1")
        cursor.execute(query % (experiment.description))
        experimentObject = cursor.fetchone()
        cursor.close()

        experimentId = experimentObject[0]
        datasetRepresentationId = experimentObject[1]
        algorithmId = experimentObject[2]
        metricId = experimentObject[3]
        combinationDescription += experimentObject[4] + "+"
        k = experiment.k

        cursor = cnx.cursor()
        query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a') order by original")
        cursor.execute(query % (datasetRepresentationId))
        documents = cursor.fetchall()
        cursor.close()

        for (document) in documents:
            documentIdsTrain.append(document[0])
            vectorsTrain.append(document[3].split(','))
            classesTrain.append(document[4])

        descriptionTest = experiment.description.split(".")[0].replace("File:Train","File:Test")

        cursor = cnx.cursor()
        query = (
        "SELECT id FROM datasetrepresentation WHERE description LIKE '%%%s%%' limit 1")
        cursor.execute(query % (descriptionTest))
        experimentObject = cursor.fetchone()
        cursor.close()

        datasetRepresentationId = experimentObject[0]

        cursor = cnx.cursor()
        query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a') order by original")
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
        combC = combC + 1

        cursor = cnx.cursor()
        addExperiment = (
            "INSERT INTO experiment_votingexperiment(experiment, votingexperiment) VALUES (%i, %i)")
        dataExperiment = (experimentId, votingExperimentId)
        cursor.execute(addExperiment % dataExperiment)
        cursor.close()
        cnx.commit()

    ensemble = VotingClassifier(estimators)
    ensemble.fit(documentsTrain,combClassesTrain[0])

    predictions = []
    c = 0
    print("Started prediction...")
    for (vectorsTest) in documentsTest[0]:
        vectorsToPredict = []
        for (temp) in documentsTest:
            vectorsToPredict.append(temp[c])

        predictions.append(ensemble.predict(vectorsToPredict))

        cursor = cnx.cursor()
        addImputation = (
            "INSERT INTO imputationvoting(document, votingexperiment, expectedClass, imputedClass) VALUES (%i, %i, '%s', '%s')")
        dataImputation = (
            combIdsTest[0][c], votingExperimentId, combClassesTest[0][c], predictions[c][0])
        cursor.execute(addImputation % dataImputation)
        cursor.close()
        c = c + 1
        cnx.commit()

    print("Completed prediction.")

    cont = cont + 1

    cursor = cnx.cursor()
    addExperiment = (
        "UPDATE votingexperiment set description = '%s', status = 'successful' WHERE id=%i")
    dataExperiment = (combinationDescription + comments, votingExperimentId)
    cursor.execute(addExperiment % dataExperiment)
    cursor.close()
    cnx.commit()

cnx.close()
cnx2.close()
cursor.close()

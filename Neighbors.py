from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import DistanceMetric
from sklearn.metrics import normalized_mutual_info_score
from scipy.stats import entropy
from scipy.stats import pearsonr
from sklearn.metrics.pairwise import cosine_similarity
from DBCredentials import DBUser, DBPassword, DBName, DBHost
from Parameters import metricName, k, train_id, document_id
import mysql.connector
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



cursor = cnx.cursor()
query = ("SELECT * FROM document where datasetRepresentation=%i AND class NOT IN('N/A','n/a') AND class NOT LIKE 'TEST:%%'")
cursor.execute(query % (train_id))
documents = cursor.fetchall()
cursor.close()

documentsTrain = documents

vectorsTrain = []
vectorsTest = []
classesTrain = []
classesTest = []
documentIdsTrain = []
documentIdsTest = []

cursor = cnx.cursor()
query = ("SELECT * FROM document where id=%i")
cursor.execute(query % (document_id))
documentsTest = cursor.fetchall()
cursor.close()

for (document) in documentsTrain:
    documentIdsTrain.append(document[0])
    vectorsTrain.append(document[3].split(','))
    classesTrain.append(document[4])

for (document) in documentsTest:
    documentIdsTest.append(document[0])
    vectorsTest.append(document[3].split(','))
    classesTest.append(document[4])

funcDist = None
if metricName == 'Cosine':
    funcDist = customCosine
if metricName == 'Jaccard':
    funcDist = customJaccard
if metricName == 'Divergence-KL':
    funcDist = customKLD

neigh = KNeighborsClassifier(n_neighbors=k, metric=funcDist)
neigh.fit(vectorsTrain, classesTrain)

for (vector) in vectorsTest:
    neighbors = neigh.kneighbors(vector, return_distance=True)
    print(neighbors)
    for (neighbor) in neighbors[1][0]:
        print(classesTrain[neighbor])

cnx.close()
cnx2.close()

from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from DBCredentials import DBUser, DBPassword, DBName, DBHost
import mysql.connector

cnx = mysql.connector.connect(user=DBUser, password=DBPassword,
                              host=DBHost,
                              database=DBName)

cursor = cnx.cursor()
query = ("DELETE FROM resultvoting")
cursor.execute(query)
cursor.close()

cursor = cnx.cursor()
query = ("SELECT id FROM votingexperiment WHERE status='successful'")
cursor.execute(query)
experiments = cursor.fetchall()
cursor.close()

#print(str(len(experiments)))

for (experiment) in experiments:
    cursor = cnx.cursor()
    query = ("SELECT id,votingexperiment,expectedClass,imputedClass FROM imputationvoting WHERE votingexperiment=%i")
    cursor.execute(query % (experiment[0]))
    documents = cursor.fetchall()
    cursor.close()

    #print(str(len(documents)))

    expectedElements = []
    imputedElements = []
    for (document) in documents:
        expectedElements.append(document[2])
        imputedElements.append(document[3])


    accuracy = accuracy_score(expectedElements,imputedElements)

   # print(str(accuracy))

    recall = recall_score(expectedElements,imputedElements, average='macro')
    precision = precision_score(expectedElements,imputedElements, average='macro')
    f1 = f1_score(expectedElements,imputedElements, average='macro')

    cursor = cnx.cursor()
    query = ("INSERT INTO resultvoting(votingexperiment,class,variable_name,variable_value) VALUES (%i,'N/A','%s',%s)")
    cursor.execute(query % (experiment[0],"accuracy",str(accuracy)))
    cursor.close()

    cursor = cnx.cursor()
    query = ("INSERT INTO resultvoting(votingexperiment,class,variable_name,variable_value) VALUES (%i,'N/A','%s',%s)")
    cursor.execute(query % (experiment[0], "precision", str(precision)))
    cursor.close()

    cursor = cnx.cursor()
    query = ("INSERT INTO resultvoting(votingexperiment,class,variable_name,variable_value) VALUES (%i,'N/A','%s',%s)")
    cursor.execute(query % (experiment[0], "recall", str(recall)))
    cursor.close()

    cursor = cnx.cursor()
    query = ("INSERT INTO resultvoting(votingexperiment,class,variable_name,variable_value) VALUES (%i,'N/A','%s',%s)")
    cursor.execute(query % (experiment[0], "f1", str(f1)))
    cursor.close()

cnx.commit()
cnx.close()





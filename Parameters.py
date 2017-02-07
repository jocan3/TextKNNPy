# metricNames = ['Divergence-KL','Cosine','Jaccard']
# algorithmName = 'KNN'
# techniques = ["No ensemble","bagging"]
# trainList = [50,75,80]
# testList = [50,25,20]
# k = 1
# increment = 10
# maxK = 32
# batch = 1

metricNames = ['Divergence-KL','Cosine','Jaccard']
algorithmName = 'KNN'
techniques = ["No ensemble","bagging"]
trainList = [50,75,80]
testList = [50,25,20]
k = 1
increment = 10
maxK = 32
batch = 1

class Experiment:
   def __init__(self, description, k):
      self.description = description
      self.k = k

votingCombinations = [
    [
        Experiment("Test",1),
        Experiment("Test",11)
    ],
    [
        Experiment("Test",1),
        Experiment("Test",11)
    ]
]


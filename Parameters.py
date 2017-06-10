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

comments = "Experiments with better recall in some classes (5 experiments)"

votingCombinations = [
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=31.",31),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:08 Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=21.",21),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 LDA only Alpha:02 Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ],
    [
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Jaccard. K=1.",1),
       Experiment("reuters-1 words vector without TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (bagging). Metric: Cosine. K=1.",1),
       Experiment("reuters-1 words vector with TF-IDF Train:75 File:Train. Algorithm: KNN (No ensemble). Metric: Cosine. K=11.",11)
    ]
]
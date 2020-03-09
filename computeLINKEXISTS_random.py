import pickle
import numpy
import math

from STB_help import *
from constants import *


def createLinkExistenceADJ():
    for i in range(max_nodes-1):
        for j in range(i, max_nodes):
            for s in S:
                dist = euclideanDistance(x_coordinates[i], y_coordinates[i], x_coordinates[j], y_coordinates[j])
                if dist < spectRange[s]:
                    LINK_EXISTS[i, j, s, :] = 1
                    LINK_EXISTS[j, i, s, :] = 1
    return 0

deploy_area = 5000
LINK_EXISTS = numpy.empty(shape=(V + NoOfDataCenters + NoOfSources, V + NoOfDataCenters + NoOfSources, numSpec, int(T/dt)))
LINK_EXISTS.fill(math.inf)


x_coordinates = numpy.array([])
y_coordinates = numpy.array([])

for i in range(max_nodes):
    x_coordinates = numpy.append(x_coordinates, (random.random()*deploy_area))
    y_coordinates = numpy.append(y_coordinates, (random.random()*deploy_area))

numpy.savetxt('Nodes_Co_ordinates.txt', numpy.c_[x_coordinates,y_coordinates], delimiter=',')
createLinkExistenceADJ()
# LINK_EXISTS = createLinkExistenceADJ_testing()


if not os.path.exists(path_to_folder):
    os.makedirs(path_to_folder)


LE_file = open(link_exists_folder + "LINK_EXISTS.pkl", 'wb')
pickle.dump(LINK_EXISTS, LE_file, protocol = 4)
LE_file.close()

print("Size of Link Exists: " + str(len(LINK_EXISTS)) + " " + str(len(LINK_EXISTS[0])) + " " + str(len(LINK_EXISTS[0][0])) + " " + str(len(LINK_EXISTS[0][0][0])))
save_in_file(link_exists_folder + "LINK_EXISTS.txt", LINK_EXISTS)
#printMAT(LINK_EXISTS)

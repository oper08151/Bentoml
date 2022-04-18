from service import IrisClassifierSerivce
from model import clf

iris_classifier_service = IrisClassifierSerivce()

iris_classifier_service.pack('model', clf)

saved_path = iris_classifier_service.save()
import logging
from Predictor import Predictor

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)
training_file = "out/2018-09-22-trainingOrient.RandOnChr1.contacts.gz.1000000.50001.500000.25000.txt"
validation_files = [
    "out/Interval_chr2_36000000_41000000validatingOrient.contacts.gz.1000000.50001.500000.25000.txt",
    "out/Interval_chr2_47900000_53900000validatingOrient.contacts.gz.1000000.50001.500000.25000.txt",
    "out/Interval_chr2_85000000_92500000validatingOrient.contacts.gz.1000000.50001.500000.25000.txt"
            ]

predictor = Predictor()
predictor.read_data_predictors(training_file)
#Some examples:
#predictor.filter_predictors(".*CTCF.*|.*RNA.*", keep=False) #-- discard CTCF AND RNA
#predictor.filter_predictors(".*CTCF.*", keep=False) #-- discard CTCF
#predictor.filter_predictors(".*contact_dist.*|.*CTCF_W.*", keep=True) #-- keep only distance and CTCF in window

trained_predictor = predictor.train(shortcut="all")
for validation_file in validation_files:
    trained_predictor.validate(validation_file)


from methods import train_voting_classifier

path = ""
# path = "_ADASYN"
# path = "_ROS"
# path = "_SMOTE"
# path = "_SMOTE_improved"

print("DetectPD" + path)
train_voting_classifier(path)

from sklearn.svm import SVC
class brain:
    def brain_processing(x,Y):
        brain = SVC(kernel='linear', random_state=0)
        brain.fit(x, Y)
        print(brain.predict([x[20]]))
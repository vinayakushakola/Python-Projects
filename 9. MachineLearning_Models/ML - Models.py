import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, r2_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import webbrowser


class MachineLearning(Tk):

    def __init__(self):
        super().__init__()
        self.title('Data Science')
        self.geometry('900x600+200+50')
        self.resizable(width=False, height=False)
        self.browseLink = tk.StringVar()
        self.feature = tk.StringVar()
        self.target = tk.StringVar()
        self.acc_output = tk.StringVar()
        self.f1_output = tk.StringVar()
        self.con_output = tk.StringVar()
        self.dropdown = tk.StringVar()
        self.webbrowser = webbrowser
        self.accuracy_score = accuracy_score
        self.r2_score = r2_score
        self.f1_score = f1_score
        self.confusion_matrix = confusion_matrix
        self.filedialog = filedialog
        self.le = LabelEncoder()

    def main(self):
        self.ML = tk.Label(self, text='Machine Learning', relief='groove', font='Verdana 33', fg='white', bg='Grey', pady=5)
        self.ML.pack(pady=(0, 30), fill='x')

        self.frame = tk.Frame(self, width=600, height=600)
        self.dataset = tk.Label(self.frame, text='Dataset', font='Verdana 20')
        self.dataset.grid(row=0, column=0)
        self.datasetE = tk.Entry(self.frame, font='Verdana 20', width=25, textvariable=self.browseLink)
        self.datasetE.grid(row=0, column=1)
        self.datasetBrowse = tk.Button(self.frame, text='B', font='Verdana 15', command=self.browse)
        self.datasetBrowse.grid(row=0, column=2)
        self.frame.pack(pady=(0, 20))

        self.frame2 = tk.Frame(self, width=600, height=600)
        self.featureL = tk.Label(self.frame2, text='Feature', font='Verdana 15')
        self.featureL.grid(row=0, column=0)
        self.featureEntry = tk.Entry(self.frame2, font='Verdana 15', textvariable=self.feature)
        self.featureEntry.grid(row=0, column=1, padx=(0, 40))

        self.targetLabel = tk.Label(self.frame2, text='Target', font='Verdana 15')
        self.targetLabel.grid(row=0, column=2)
        self.targetEntry = tk.Entry(self.frame2, font='Verdana 15', textvariable=self.target)
        self.targetEntry.grid(row=0, column=3)
        self.frame2.pack(pady=(20))

        self.choices = {'Linear Regression', 'Logistic Regression', 'Decision Tree', 'Random Forest'}
        self.dropdown.set('Model')
        self.popupMenu = tk.OptionMenu(self, self.dropdown, *self.choices)
        self.popupMenu.config(width='20', height=2)
        self.popupMenu.pack(pady=20)

        self.frame3 = tk.Frame(self)
        self.runB = tk.Button(self.frame3, text='Run', font='Verdana 15', relief='ridge', command=self.run)
        self.runB.grid(row=0, column=0, padx=(0, 20))
        self.predictionB = tk.Button(self.frame3, text='Prediction', font='Verdana 15', relief='ridge', command=self.accuracy)
        self.predictionB.grid(row=0, column=1, padx=(20, 0))
        self.frame3.pack()

        self.frame4 = tk.Frame(self)
        self.accuracyB = tk.Button(self.frame4, text='Accuracy', font='Verdana 12', relief='groove', width=14, command=self.accuracy)
        self.accuracyB.grid(row=0, column=0, pady=(0, 20), padx=(0, 20))
        self.accuracyE = tk.Entry(self.frame4, font='Verdana 15', textvariable=self.acc_output)
        self.accuracyE.grid(row=0, column=1, pady=(0, 20))

        self.f1scoreB = tk.Button(self.frame4, text='F1 Score', font='Verdana 12', relief='groove', width=14, command=self.f1score)
        self.f1scoreB.grid(row=1, column=0, pady=(0, 20), padx=(0, 20))
        self.f1scoreE = tk.Entry(self.frame4, font='Verdana 15', textvariable=self.f1_output)
        self.f1scoreE.grid(row=1, column=1, pady=(0, 20))

        self.confmatB = tk.Button(self.frame4, text='Confusion Matrix', relief='groove', font='Verdana 12', command=self.confusionmatrix)
        self.confmatB.grid(row=2, column=0, pady=(0, 20), padx=(0, 20))
        self.confmatL = tk.Label(self.frame4, font='Verdana 15', bg='white', textvariable=self.con_output)
        self.confmatL.grid(row=2, column=1, pady=(0, 20))
        self.frame4.pack(pady=(30,0))


    def browse(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("all files", "*.*"), ("jpeg files", "*.jpg")))

        self.browseLink.set(self.filename)
        self.webbrowser.open(self.filename)
        self.df = pd.read_csv(r'{}'.format(self.filename))

    def run(self):
        if self.dropdown.get() == 'Linear Regression':
            f = self.feature.get().split(',')

            for i in f:
                if self.df[i].isnull().sum() != 0:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.df[i].fillna(self.df[i].mode()[0])
                        self.df[i] = self.le.fit_transform(self.df[i])
                    else:
                        self.df[i] = self.df[i].fillna(self.df[i].mean())
                else:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.le.fit_transform(self.df[i])

            self.X = self.df[self.feature.get().split(',')]
            self.y = self.df[self.target.get()]

            self.model = LinearRegression()
            self.model.fit(self.X, self.y)

            self.pred = self.model.predict(self.X)


        elif self.dropdown.get() == 'Logistic Regression':
            f = self.feature.get().split(',')

            for i in f:
                if self.df[i].isnull().sum() != 0:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.df[i].fillna(self.df[i].mode()[0])
                        self.df[i] = self.le.fit_transform(self.df[i])
                    else:
                        self.df[i] = self.df[i].fillna(self.df[i].mean())
                else:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.le.fit_transform(self.df[i])

            self.X = self.df[self.feature.get().split(',')]
            self.y = self.df[self.target.get()]

            self.model = LogisticRegression()
            self.model.fit(self.X, self.y)

            self.pred = self.model.predict(self.X)


        elif self.dropdown.get() == 'Decision Tree':
            f = self.feature.get().split(',')

            for i in f:
                if self.df[i].isnull().sum() != 0:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.df[i].fillna(self.df[i].mode()[0])
                        self.df[i] = self.le.fit_transform(self.df[i])
                    else:
                        self.df[i] = self.df[i].fillna(self.df[i].mean())
                else:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.le.fit_transform(self.df[i])

            self.X = self.df[self.feature.get().split(',')]
            self.y = self.df[self.target.get()]

            self.model = DecisionTreeClassifier()
            self.model.fit(self.X, self.y)

            self.pred = self.model.predict(self.X)

        elif self.dropdown.get() == 'Random Forest':
            f = self.feature.get().split(',')

            for i in f:
                if self.df[i].isnull().sum() != 0:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.df[i].fillna(self.df[i].mode()[0])
                        self.df[i] = self.le.fit_transform(self.df[i])
                    else:
                        self.df[i] = self.df[i].fillna(self.df[i].mean())
                else:
                    if self.df[i].dtypes == 'object':
                        self.df[i] = self.le.fit_transform(self.df[i])

            self.X = self.df[self.feature.get().split(',')]
            self.y = self.df[self.target.get()]

            self.model = RandomForestClassifier()
            self.model.fit(self.X, self.y)

            self.pred = self.model.predict(self.X)

    def prediction(self):
        self.data = pd.DataFrame({'Actual': self.y, 'Predicted': self.pred})
        self.data.to_csv('pred.csv', index=False)
        self.webbrowser.open('pred.csv')

    def accuracy(self):
        if self.dropdown.get() == 'Linear Regression':
            self.acc_output.set(r2_score(self.pred, self.y))
        else:
            self.acc_output.set(accuracy_score(self.pred, self.y))

    def f1score(self):
        self.f1_output.set(f1_score(self.pred, self.y))

    def confusionmatrix(self):
        self.con_output.set(confusion_matrix(self.pred, self.y))


if __name__ == '__main__':
    root = MachineLearning()
    root.main()
    root.mainloop()


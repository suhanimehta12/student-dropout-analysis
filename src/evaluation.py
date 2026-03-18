from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


def evaluate_models(models, X_train, X_test, y_train, y_test):

    results = []

    for name, model in models.items():

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        acc = accuracy_score(y_test, predictions)

        results.append({
            "Model": name,
            "Accuracy": acc
        })

        print(name)
        print(classification_report(y_test, predictions))

    return pd.DataFrame(results)
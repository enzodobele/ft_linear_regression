creer le venv : python3 -m venv venv
pour lancer le venv : source venv/bin/activate
pour installer les dependances : pip install -r requirements.txt

a 42 :  python3 -m venv /goinfre/$USER/venv_ft_lr
        source /goinfre/$USER/venv_ft_lr/bin/activate
        pip install -r requirements.txt

estimatePrice(mileage) = θ0 + (θ1 × mileage) est l'équation d'une droite (y = ax + b).

θ0 (theta0) = l'ordonnée à l'origine → le prix estimé pour une voiture à 0 km.

θ1 (theta1) = la pente de la droite → de combien le prix varie pour chaque km supplémentaire. Dans ce cas il sera négatif (plus de km → prix qui baisse).

tmpθ0 = learningRate × (1/m) × Σ(estimatePrice(mileage[i]) − price[i])

tmpθ1 = learningRate × (1/m) × Σ(estimatePrice(mileage[i]) − price[i]) × mileage[i]

learningRate est la force de correction lors d'une itération.
on le multiple par 1 divisé par le nombre de valeur utiliser dans chaque itération (içi 24)

On multiple ça ensuite par somme (Σ) des erreurs sur chaque valeur du dataset.

pour theta1 on multiplie chaqu'une des erreurs par le mileage qui a servit a calculer l'erreur avant de l'ajouter au sum.
(θ0 + (θ1 × mileage))





Normalisation:
la normalisation revient a redimentionner ces valeur en considérant la plus petite comme 0 et la plus haute comme 1

On évite ainsi de travailler avec des valeurs qui nous ferais atteindre des valeurs beaucoup trop haute lors de l'entrainement.

On dénormalise ensuite pour que l'entrée utilisateur corresponde a des valeurs cohérente

ex :    mileage = 0 - price = 100
        mileage = 10 - price = 0
        theta1 = (0 - 100) / (10 - 0) = -10
        le prix baisse de 10€ par km
        donc de 100€ pour 10km

        quand on normalise :
        mileage = 0 - price = 100
        mileage = 1 - price = 0
        theta1_norm = (0 - 100) / (1 - 0) = -100
        de 0 à 1 je perd 100€
        donc par tranche de 0.1 je perd 10€




MAE pour Mean Absolute Error (erreur absolue moyenne):

Pour le calculer on fait juste un tour comme pour l'entrainement en récupérant seulement la valeur absolue de la différence : 
MAE = (1/m) × Σ |estimatePrice(mileage[i]) - price[i]|

les | | désigne la valeur absolue. 
On l'utilise pour eviter d'annuler les valeurs.
ex :    vrai prix : 5000, notre modèle prédit 5500 donc + 500
                puis
        vrai prix : 8000, notre modèle prédit 7500 donc - 500
l'erreur = 500 + (-500) donc 0 alors que l'erreur est de 500 + 500 donc 1000




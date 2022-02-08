def compute_pi(p):
    result = 0
    n = 0
    old_result = 1
    precision = 10 ** -p

    # TODO calculer la valeur de pi d'après la formule donnée dans l'énoncé

    return result, n

if __name__ == '__main__':
    # Calcul de π (pi)
    pi = 3.141592653589793
    p = 5
    computed_pi , nb_iter = compute_pi(p)
    print("La valeur réel de pi est : {}".format(pi))
    print("La valeur approché de pi à 10e-{} est : {}".format(p, computed_pi))
    print("Résultat obtenu après {} itérations".format(nb_iter))
# Calculo de numero primo mediante lenguaje R
from rpy2.robjects import r

def numeros_primos(n):
    r.assign('n', n)
    r('''
    print("Numeros primos: ")
    for(i in 2:n){
        prime = TRUE
        for (j in 2:(i-1)){
            if (i %% j == 0){
                prime = FALSE
            }
        }
        if (prime == TRUE){
            print(i)
        }
    }
    ''')


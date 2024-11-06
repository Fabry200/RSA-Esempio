
# Congruenze Lineari e Crittografia RSA

Questo progetto implementa algoritmi di congruenze lineari e crittografia RSA utilizzando il modulo `congruenzelineari.py`. La crittografia RSA è un algoritmo di cifratura asimmetrica che si basa su operazioni di congruenza mod N, dove N è il prodotto di due numeri primi.

## Funzionalità

### 1. **Trova chiavi pubbliche valide**

La funzione `findpub(N, fiN, numkeys)` trova tutte le chiavi pubbliche valide (intere) che sono coprime con \( N \) e con \( \phi(N) \) (dove \( \phi(N) \) è la funzione di Eulero di N). Restituisce una lista di chiavi pubbliche fino al numero richiesto.

### 2. **Genera coppie di chiavi**

La funzione `keys(e, fiN, N)` genera la coppia di chiavi per la crittografia RSA. La chiave pubblica è formata da una coppia \([e, N]\), mentre la chiave privata è generata utilizzando l'inverso di \( e \) modulo \( \phi(N) \).

### 3. **Crittografia**

La funzione `crypt(m, e)` cifra un messaggio `m` usando la chiave pubblica \([e, N]\), con il seguente algoritmo di crittografia RSA: \( c = m^e \mod N \).

### 4. **Decifratura**

La funzione `decrypt(m, couple, N, e)` decifra il messaggio cifrato `m` utilizzando la chiave privata `couple[0]` e il modulo \( N \), seguendo il processo inverso della crittografia RSA: \( m = c^{\text{private\_key}} \mod N \).

## Funzioni Principali

### `findpub(N, fiN, numkeys)`

Trova le prime chiavi che sono coprime sia con \( \phi(N) \) che con \( N \).

**Parametri**:
- `N` (int): Il prodotto di due numeri primi (modulo RSA).
- `fiN` (int): La funzione di Eulero \( \phi(N) \).
- `numkeys` (int): Il numero di chiavi pubbliche da restituire.

**Restituisce**:
- Una lista di chiavi pubbliche.

### `keys(e, fiN, N)`

Genera la coppia di chiavi pubbliche e private.

**Parametri**:
- `e` (int): La chiave pubblica.
- `fiN` (int): La funzione di Eulero \( \phi(N) \).
- `N` (int): Il modulo RSA.

**Restituisce**:
- La chiave pubblica come coppia `[e, N]` e la chiave privata come coppia `[private_key, N]`.

### `crypt(m, e)`

Cifra il messaggio `m` usando la chiave pubblica.

**Parametri**:
- `m` (list): Il messaggio da cifrare, rappresentato come una lista di numeri.
- `e` (int): La chiave pubblica.

**Restituisce**:
- Una lista di messaggi cifrati.

### `decrypt(m, couple, N, e)`

Decifra il messaggio `m` usando la chiave privata.

**Parametri**:
- `m` (list): Il messaggio cifrato, rappresentato come una lista di numeri.
- `couple` (list): La coppia di chiavi (privata e pubblica).
- `N` (int): Il modulo RSA.
- `e` (int): La chiave pubblica.

**Restituisce**:
- Il messaggio decifrato.

## Esempio di utilizzo

```python
def main():
    p = 557 
    q = 307
    N = p * q
    fiN = (p - 1) * (q - 1)
    e = 31  # 1 < e < fiN tale che e è primo con N
    m = [3, 9, 1, 13]
    
    # Genera la coppia di chiavi
    couple = cl.trovasol(e, 1, fiN)
    
    # Trova le chiavi pubbliche
    print(findpub(N, fiN, 100))
    
    # Stampa le chiavi
    print(keys(e, fiN, N))
    
    # Cifra il messaggio
    print(crypt(m, e))
    
    # Decifra il messaggio
    print(decrypt(m, couple, N, e))
    
main()

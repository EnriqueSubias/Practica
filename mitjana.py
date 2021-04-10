
import sys

def mitjana(alcades):
   resultat = 0
   for x in alcades:
      resultat += x
   return resultat / len(alcades)

if __name__ == "__main__":
   in_alcades = []
   for line in open(sys.argv[1]):
      nom, alcada = line.split()
      in_alcades += [alcada]

   print mitjana([int(x) for x in in_alcades])


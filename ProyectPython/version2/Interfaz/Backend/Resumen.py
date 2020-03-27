# Importa los metodos a trabajar desde NLTK:
import nltk
# stopwords = palabras reservadas.
from nltk.corpus import stopwords

# word_tokenize = valorizador de palabras.
# sent_tokenize = valorizador de oraciones.
from nltk.tokenize import word_tokenize, sent_tokenize

# Descarga de metodos debido a que stopwords y tokenize
#   no se podían usar sin ellos.

#nltk.download('stopwords')
#nltk.download('punkt')
class Resumen(object):

    def tablaFrecuencias(self, t1):
        # Se crean 2 arreglos y 1 variable:

        # arreglo 1) - SW - configura el método de entrada o idioma en el que se 
                            # van a trabajar las palabras en el metodo words de stopwords, en este caso, Español.
        SW = set(stopwords.words("spanish"))

        # text para definir el texto a resumir.
        text=t1
        # arreglo 2) - words - almacena el texto en el método word_tokenize para 
                                # previamente darle valor.
        words = word_tokenize(text)


        # Se crea un diccionario para crear una tabla de frecuencias de las palabras.
        freqTable = dict()

        # Con un for se recorre el texto y se almacena en la tabla.
        for word in words:
            word = word.lower() # setea las palabras en minúscula y las almacena en word.
            if word in SW: 
                continue # Si la palabra se encuentra en SW, continua con el ciclo.
            if word in freqTable: # Si la palabra ya se encuentra en la tabla frecuencia,
                freqTable[word] += 1 # Suma 1 a la posición donde se encuentra la palabra.
            else:
                freqTable[word] = 1 # Sino, la palabra en la TF va a ser igual a 1.

        #Muestra la tabla de frecuencias de cada palabra.
        #freqTable
        print(freqTable)
        return freqTable

    def oracionesYvalorizacion(self, freqTable2, text1):

        # Crea una variable y un diccionario.

        # Variable sentences para almacenar las oraciones a valorizar del texto.
        sentences = sent_tokenize(text1)

        # Diccionario sentenceValue para almacenar los valores de las oraciones.
        sentenceValue = dict()

        #Se crea un ciclo for para recorrer las oraciones que se encuentran en el texto.
        for sentence in sentences:
            # Se crea un segundo for para recorrer los items que se encuentran el la TF.
            for word, freq in freqTable2.items():
                if word in sentence.lower(): # Si la palabra se encuentra en las oraciones (en minuscula)
                    if sentence in sentenceValue: # Y si la oración está en el diccionario de las oraciones a valorizar.
                        sentenceValue[sentence] += freq # Entonces sume 1 al número de frecuencia en la posición de la oración del sV.
                    else:
                        sentenceValue[sentence] = freq # Sino, que el valor de la posición de la oración sea igual a la frecuencia.

        #Muestra las oraciones ya valorizadas con su respectivo puntaje.
        #sentenceValue

        print(sentenceValue)
        return sentenceValue

    def resumir(self, texto):
        table=self.tablaFrecuencias(texto)
        sentenceValue2=self.oracionesYvalorizacion(table, texto)
        sentences = sent_tokenize(texto)
        # Se crea una variable donde se almacena la suma de los valores.
        sumValues = 0

        # Se crea un ciclo for para evaluar la oración dentro del Diccionario de las oraciones valorizadas.
        for sentence in sentenceValue2:
            sumValues += sentenceValue2[sentence] # Se suma 1 al valor de la Oración en su respectiva posición
            
        # Valor promedio de una oración desde un texto original
        average = int(sumValues/ len(sentenceValue2)) # Divide la suma de valores en la total de oraciones valorizadas.

        # Se crea una variable para almacenar el resumen a imprimir.
        summary = ''

        # Se crea un for para recorrer las oraciones almacenadas
        for sentence in sentences:
            
            #Donde si, la oración está las oraciones Valorizadas y la posición de la oración es mayor que 1.2 veces el promedio:
            if (sentence in sentenceValue2) and (sentenceValue2[sentence] > (1.2 * average)):
                
                # El resumen va a agregar un espacio más la oración que aprobó la condición.
                summary += " " + sentence

        # Se imprime el resumen.
        res=str("\n"+"\n"+summary)
        print("\n"+"\n"+summary)
        return res, table
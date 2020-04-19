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


# Se crean 2 arreglos y 1 variable:

# arreglo 1) - SW - configura el método de entrada o idioma en el que se 
                    # van a trabajar las palabras en el metodo words de stopwords, en este caso, Español.
SW = set(stopwords.words("spanish"))

# text para definir el texto a resumir.
text = """En informática , la inteligencia artificial ( IA ), a veces llamada inteligencia de máquina , es inteligencia demostrada por máquinas , en contraste con la inteligencia natural que muestran los humanos y los animales . Los principales libros de texto de IA definen el campo como el estudio de los " agentes inteligentes ": cualquier dispositivo que perciba su entorno y tome medidas que maximicen sus posibilidades de lograr con éxito sus objetivos. [1]Coloquialmente, el término "inteligencia artificial" se usa a menudo para describir máquinas (o computadoras) que imitan funciones "cognitivas" que los humanos asocian con la mente humana , como "aprendizaje" y "resolución de problemas". A medida que las máquinas se vuelven cada vez más capaces, las tareas que se consideran que requieren "inteligencia" a menudo se eliminan de la definición de IA, un fenómeno conocido como efecto de IA . [3] Una broma en el Teorema de Tesler dice que "AI es lo que no se ha hecho todavía". [4] Por ejemplo, el reconocimiento óptico de caracteres a menudo se excluye de las cosas consideradas como AI [5] , convirtiéndose en una tecnología de rutina. [6] Las capacidades modernas de la máquina generalmente clasificadas como IA incluyen la comprensión exitosa del habla humana , [7] competir al más alto nivel en los sistemas de juego estratégico (como el ajedrez y el Go)), [8] vehículos autónomos , enrutamiento inteligente en redes de entrega de contenido y simulaciones militares.La inteligencia artificial fue fundada como una disciplina académica en 1955, y en los años transcurridos desde entonces ha experimentado varias oleadas de optimismo, [9] [10] seguido por la decepción y la pérdida de fondos (conocido como un " invierno AI "), [11] [12] seguido de nuevos enfoques, éxito y financiación renovada. [10] [13] Durante la mayor parte de su historia, la investigación de IA se ha dividido en subcampos que a menudo no se comunican entre sí. [14] Estos subcampos se basan en consideraciones técnicas, como objetivos particulares (por ejemplo, " robótica " o " aprendizaje automático "), [15] el uso de herramientas particulares (" lógica"o redes neuronales artificiales ), o profundas diferencias filosóficas. [16] [17] [18] Los subcampos también se han basado en factores sociales (instituciones particulares o el trabajo de investigadores particulares). """

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



# Crea una variable y un diccionario.

# Variable sentences para almacenar las oraciones a valorizar del texto.
sentences = sent_tokenize(text)

# Diccionario sentenceValue para almacenar los valores de las oraciones.
sentenceValue = dict()

#Se crea un ciclo for para recorrer las oraciones que se encuentran en el texto.
for sentence in sentences:
    # Se crea un segundo for para recorrer los items que se encuentran el la TF.
    for word, freq in freqTable.items():
        if word in sentence.lower(): # Si la palabra se encuentra en las oraciones (en minuscula)
            if sentence in sentenceValue: # Y si la oración está en el diccionario de las oraciones a valorizar.
                sentenceValue[sentence] += freq # Entonces sume 1 al número de frecuencia en la posición de la oración del sV.
            else:
                sentenceValue[sentence] = freq # Sino, que el valor de la posición de la oración sea igual a la frecuencia.

#Muestra las oraciones ya valorizadas con su respectivo puntaje.
#sentenceValue

print(sentenceValue)

# Se crea una variable donde se almacena la suma de los valores.
sumValues = 0

# Se crea un ciclo for para evaluar la oración dentro del Diccionario de las oraciones valorizadas.
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence] # Se suma 1 al valor de la Oración en su respectiva posición
    
# Valor promedio de una oración desde un texto original
average = int(sumValues/ len(sentenceValue)) # Divide la suma de valores en la total de oraciones valorizadas.

# Se crea una variable para almacenar el resumen a imprimir.
summary = ''

# Se crea un for para recorrer las oraciones almacenadas
for sentence in sentences:
    
    #Donde si, la oración está las oraciones Valorizadas y la posición de la oración es mayor que 1.2 veces el promedio:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        
        # El resumen va a agregar un espacio más la oración que aprobó la condición.
        summary += " " + sentence

# Se imprime el resumen.
print("\n"+"\n"+summary)
Data Engineer Challenge - LATAM Airlines
Instrucciones:
1. Tu desafío debe tener al menos UN archivo jupyter notebook (.ipynb) con la resolución identificando claramente los distintos ejercicios.
2. Puedes utilizar el lenguaje que prefieras, pero los desafíos con Python serán mejores rankeados.
3. Puedes utilizar las tecnologías y técnicas que prefieras para el procesamiento de datos. Incluso servicios cloud. En tal caso, procura seguir el paso a paso en tu jupyter notebook SIN agregar las credenciales de acceso a los distintos servicios.
4. Los desafíos que posean un orden claro, sean explicativos, modulares, eficientes y creativos serán mejor rankeados.
5. Recuerda que no estamos en tu cabeza! Escribe los supuestos que estás asumiendo.
6. Para este desafío te recomendamos que describas claramente cómo mejorar cada parte
de tu ejercicio en caso de que tenga opción de mejora.
7. Debes utilizar los datos contenidos en el siguiente archivo.
8. Puedes utilizar la documentación oficial de twitter para entender la estructura de los
datos.
9. Tu solución debe estar en un repositorio público de la plataforma de git de tu
preferencia. Enviar link a mail esteban.castillo@latam.com
10. Evaluaremos positivamente las buenas prácticas de uso de git. Tus commits, branches,
pull requests.
11. Asunto: Data-Engineer-challenge - [tuNombre]-[tuApellido]
12. Éxito!
   
 Desafío:
En el archivo encontrarás un conjunto aproximado de 389MBs. Se pide calcular lo siguiente:
1. Los top 10 tweets más retweeted.
2. Los top 10 users en función a la cantidad de tweets que emitieron.
3. Los top 10 días donde hay más tweets.
4. Los top 10 hashtags más usados.
5. Los top 10 emojis más usados.
6. Los top 10 users más influyentes en función de lo retweeted de sus tweets.





------------------------------------------------



In this repository you will find the responses to the above excersice as follows:

LATAMTest.ipynb: The main execution with all the results.

tweetprocessclass.py: The different functions created to perform all tasks.

tweetprocessclassEXPLAINED.ipynb: All the functions explained step by step.

docker-compose.yml: docker compose required to generate a DB for the added steps.

tweets-json.json.zip: list of tweets as zip in order to be able to upload it to GitHub.



Requirements:


Python v 3.0

Anaconda Jupyter notebooks 6.1.4 or google collab


Implementation:


Clone repository to local enviroment

Run 'LATAMTest.ipynb' 


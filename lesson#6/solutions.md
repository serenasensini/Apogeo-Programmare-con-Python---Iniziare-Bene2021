# Lezione #5

## Soluzione n.1
Correggere il seguente codice:

```
list = [10, 20, 30, 40, 50, 60, 70]

counter = 0
for element in list: 
    if element % 5 == 0:
        counter += 1
        
print(counter)
```

## Soluzione n.2

Correggere il seguente codice:

```
lst = ['Alice', 'Bob', 'Carl']
print(lst[2])
```


## Soluzione n.3

Correggere il seguente codice:

```
tupla = ('Alice', 'Bob')
print(tupla[1])
```

## Soluzione n.4

Correggere il seguente codice:

```
def area_cerchio(raggio):
    print(3.14*raggio**2)

def circonferenza(raggio):
    print(3.14*raggio*2)

area_cerchio(3)
circonferenza(4)
```

## Soluzione n.5

Correggere il seguente codice:

```
def moltiplicazione(a,b):
    print a*b

moltiplicazione(1,2)

```

## Soluzione n.6

Definire una classe che rappresenti un utente e i relativi attributi, come lo username, la mail e la data di nascita.

```
class Utente:

    def __init__(self, nickname, mail, data_nascita):
        self.nickname = nickname
        self.mail = mail
        self.data_nascita = data_nascita
        
    def __repr__(self):
        print("--------------")
        print("Nome utente:", self.nickname)
        print("Mail:", self.mail)
        print("Data di nascita:", self.data_nascita)
        print("-------------")
        
    def get_nickname(self):
        return self.nickname
    
    def get_mail(self):
        return self.mail
    
    def get_data_nascita(self):
        return self.data_nascita
    
    def set_nickname(self, nickname):
        self.nickname = nickname
        
    def set_mail(self, mail):
        self.mail = mail
        
    def set_data_nascita(self, data_nascita):
        self.data_nascita = data_nascita
```

## Soluzione n.7 

Definire una classe che rappresenti un auto e i relativi attributi, come la marca, il modello, l'anno di immatricolazione e il numero di porte.

## Soluzione n.8

Definire una classe che rappresenti un film: includere il regista, l'anno di distribuzione, un elenco di attrici e attori, il titolo e il genere. Includere i metodi setter e getter per ciascuna proprietà, e definire anche un metodo per stamparne i dettagli.

## Soluzione n.9

Definire una classe che rappresenti un immobile, con le relative proprietà (locali, bagni, garage (si/no), piano, quartiere) e includere i metodi setter e getter per ciascuna proprietà; definire anche un metodo per stamparne i dettagli.

## Soluzione n.10 

Definire una classe per rappresentare un/a regista, che ne includa le proprietà anagrafiche ed anche i film girati. Includere i metodi setter e getter per ciascuna proprietà, e definire anche un metodo per stamparne i dettagli.

## Gioco!

```
class Quiz:

    def __init__(self, questions):
        self.questions = questions

    def startQuiz(self):
        print("Ready to start? Three... Two.. One. GO!")
        score = 0
        for question, answer in self.questions.items():
            user_answer = input(question + " ")
            if user_answer == answer:
                score += 1
                print("Congrats! You're score now is:", score)
            else:
                print("Ops! Wrong answer. You're score is still:", score)
        print("Game over!")

    def setQuestions(self, questions):
        self.questions = questions

    def getQuestion(self, question):
        return self.questions[question]

    def __repr__(self):
        print(self.questions)


questions = {
    "Quanto fa 5 x 2?": "10",
    "Qual è la radice quadrata di 64?": "8",
    "Quanti sono stati i re di Roma?": "7"
}

quiz = Quiz(questions)
quiz.startQuiz()



```
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def func1():
    s=int(input())
    movie = movies[s]
    if movie["imdb"]>5.5:
           return True
    return False
print(func1())


def func2():
     
      for mov in movies:
            if mov["imdb"]>5.5:
                  print(mov)
func2()

def func3():
     cat=input()
     for x in movies:
           if x["category"]==cat:
                 print(x["name"])
func3()

def func4():
      s=0
      cnt=0
      for x in movies:
            s=(s+x["imdb"])
            cnt+=1
            
      print(s/cnt)
func4()

def func5():
      s=0
      cnt=0
      cat=input()
      for x in movies:
            if x["category"]== cat:
                  s=s+x["imdb"]
                  cnt+=1
      print(s/cnt)
func5()     
      
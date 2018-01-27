import json

A = {
    "MovieName": "Alien",
    "Year": 1979,
    "Director": {
        "FirstName": "Ridley",
        "LastName": "Scott"
    },
    "IMDBGrade": 8.5,
    "Stars": [
        "Sigourney Weaver",
        "Tom Skeritt",
        "John Hurt"
    ]
}

inputJSON = """{"MovieName": "Alien",
    "Year": 1979,
    "Director": {
        "FirstName": "Ridley",
        "LastName": "Scott"
    },
    "IMDBGrade": 8.5,
    "Stars": [
        "Sigourney Weaver",
        "Tom Skeritt",
        "John Hurt"
    ]
}"""

report_str = """Alien
-----
Year: 1979
Director: Ridley Scott
IMDB grade: 8.5
Stars: Sigourney Weaver, Tom Skeritt, John Hurt
"""

def build_report(obj):
    movie_name = obj["MovieName"]
    report = "%s\n%s" % (movie_name, '-' * len(movie_name))
    report += "\nYear: " + str(obj["Year"])
    d = obj["Director"]
    report += "\nDirector: %s %s" % (d["FirstName"], d["LastName"])
    report += "\nIMDB grade: %1.1f" % obj["IMDBGrade"]
    report += "\nStars: " + ', '.join(obj['Stars']) + '\n'
    return report

B = json.loads(inputJSON)
Atxt = build_report(A)
Btxt = build_report(B)

assert(Atxt==Btxt)
assert(Atxt==report_str)


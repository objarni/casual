import json

'''
1. Include an in-code object literal
   equal to input.json content --> A
2. Read input.json --> B
3. Produce a report string from A and B --> Atxt, Btxt
4. Verify Atxt == Btxt
5. Verify Atxt equals content of report.txt
'''

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

'''
Alien
-----
Year: 1979
Director: Ridley Scott
IMDB grade: 8.5
Stars: Sigourney Weaver, Tom Skerritt, John Hurt
'''


def build_report(obj):
    movie_name = obj["MovieName"]
    report = "%s\n%s" % (movie_name, '-' * len(movie_name))
    report += "\nYear: " + str(obj["Year"])
    d = obj["Director"]
    report += "\nDirector: %s %s" % (d["FirstName"], d["LastName"])
    report += "\nIMDB grade: %1.1f" % obj["IMDBGrade"]
    report += "\nStars: " + ', '.join(obj['Stars']) + '\n'
    return report


def selftest():
    with open('input.json') as f:
        content = f.read()
    B = json.loads(content)
    Atxt = build_report(A)
    Btxt = build_report(B)

    assert(Atxt==Btxt)
    with open('report.txt') as f:
        expected = f.read()
    assert(Atxt==expected)


if __name__ == '__main__':
    selftest()

JSON = (loadfile "JSON.lua")()

local A = {
    MovieName="Alien",
    Year=1979,
    Director={
        FirstName="Ridley",
        LastName="Scott"
    },
    IMDBGrade=8.5,
    Stars={
        "Sigourney Weaver",
        "Tom Skeritt",
        "John Hurt"
    }
}

local inputJSON = [[{
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
}]]

local report_str = [[
Alien
-----
Year: 1979
Director: Ridley Scott
IMDB grade: 8.5
Stars: Sigourney Weaver, Tom Skeritt, John Hurt
]]

function build_report(obj)
    local movie_name = obj.MovieName
    local underline = '-----'
    local report = ("%s\n%s"):format(movie_name, underline)
    report = report .. "\nYear: " .. tostring(obj.Year)
    local d = obj.Director
    report = report .. ("\nDirector: %s %s"):format(d.FirstName, d.LastName)
    report = report .. ("\nIMDB grade: %1.1f"):format(obj.IMDBGrade)
    report = report .. "\nStars: "
    for ix,star in ipairs(obj.Stars) do
        report = report .. star
        if ix < #obj.Stars then
            report = report .. ', '
        end
    end
    return report .. '\n'
end

local B = JSON:decode(inputJSON)
local Atxt = build_report(A)
local Btxt = build_report(B)

assert(Atxt==Btxt)
assert(Atxt==report_str)

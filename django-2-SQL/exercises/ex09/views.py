from django.http import HttpResponse
from django.db import connection 


def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.name, p.homeworld, pl.climate
            FROM ex09_people p
            INNER JOIN ex09_planets pl ON CAST(p.homeworld AS INTEGER) = pl.id
            WHERE pl.climate LIKE '%windy%'
            ORDER BY p.name;
            """)
            rows = cursor.fetchall()

        if not rows:
            return HttpResponse("No data available")

        result = "<table border='1'>"
        result += "<tr><th>Name</th><th>Homeworld</th><th>Climate</th></tr>"
        for row in rows:
            result += (
                f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
            )
        result += "</table>"
        return HttpResponse(result)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

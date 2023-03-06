WITH midList(mids) as (
        (SELECT DISTINCT movieID 
        FROM MOVIE
        WHERE name LIKE '%{n}%')
        UNION 
        (SELECT DISTINCT movieID
        FROM ACTS natural join ACTOR
        WHERE name LIKE '%{n}%')
        UNION 
        (SELECT DISTINCT movieID
        FROM DIRECTOR natural join DIRECTS
        WHERE name LIKE '%{n}%')
        )

        SELECT *
        FROM MOVIE as m, midList,ACTOR a, ACTS ar, DIRECTOR d, DIRECTS dr 
        WHERE ar.actorID  = a.actorID and ar.movieID = m.movieID and 
        dr.directorID  = d.directorID and dr.movieID = m.movieID and
        m.movieID = midList.mids;